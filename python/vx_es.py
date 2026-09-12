"""VX–ES: fit a dollar hedge, then trade the VIX minus VX basis.

1. Align VX and ES on dates, scatter, OLS-fit after Aug 2008.
2. If the basis is wide vs days-to-expiry, long/short VX hedged with ES.

Lecture hedge: regress 50*ES on 1000*VX + intercept → slope ≈ -0.3507.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from helpers import ann_return, sharpe

ES_MULT = 50.0    # dollars per ES point
VX_MULT = 1000.0  # dollars per VX point
HEDGE = 0.3507    # |beta| from the lecture fit
THRESH_PER_DAY = 0.1


def align_on_date(vx: pd.Series, es: pd.Series) -> pd.DataFrame:
    """Inner join on the index (dates)."""
    return pd.concat({"VX": vx, "ES": es}, axis=1).dropna()


def fit_hedge(vx: pd.Series, es: pd.Series) -> float:
    """Regress 50*ES on 1000*VX plus an intercept. Returns slope on VX."""
    y = ES_MULT * es.to_numpy(dtype=float)
    x = np.column_stack(
        [VX_MULT * vx.to_numpy(dtype=float), np.ones(len(vx))]
    )
    beta, *_ = np.linalg.lstsq(x, y, rcond=None)
    return float(beta[0])


def roll_per_day(vix: pd.Series, vx: pd.Series, dte: pd.Series) -> pd.Series:
    """(VIX - VX) / trading days to settlement."""
    return (vix - vx) / dte


def positions(vix: pd.Series, vx: pd.Series, dte: pd.Series) -> pd.DataFrame:
    """
    If VIX - VX > 0.1 * DTE  -> buy 0.3507 VX and buy 1 ES
    If VX - VIX > 0.1 * DTE  -> short both
    Hold 1 day.
    """
    gap = vix - vx
    thresh = THRESH_PER_DAY * dte
    pos_vx = pd.Series(0.0, index=vix.index)
    pos_es = pd.Series(0.0, index=vix.index)

    cheap = gap > thresh          # future cheap -> expected +roll
    rich = (-gap) > thresh        # future rich  -> expected -roll
    pos_vx[cheap] = HEDGE
    pos_es[cheap] = 1.0
    pos_vx[rich] = -HEDGE
    pos_es[rich] = -1.0
    return pd.DataFrame({"pos_vx": pos_vx, "pos_es": pos_es})


if __name__ == "__main__":
    idx = pd.bdate_range("2009-01-02", periods=6)
    demo = pd.DataFrame(
        {
            "VIX": [20, 21, 19, 18, 25, 24],
            "VX": [22, 21.5, 18, 16, 23, 26],
            "ES": [900, 910, 930, 940, 880, 870],
            "dte": [15, 14, 13, 12, 11, 10],
        },
        index=idx,
    )
    print("hedge slope (lecture was -0.3507):",
          round(fit_hedge(demo["VX"], demo["ES"]), 4))
    print(positions(demo["VIX"], demo["VX"], demo["dte"]))

    pos = positions(demo["VIX"], demo["VX"], demo["dte"]).shift(1)
    vx_pnl = pos["pos_vx"] * demo["VX"].diff() * VX_MULT
    es_pnl = pos["pos_es"] * demo["ES"].diff() * ES_MULT
    # Notional ~ one ES contract so APR/Sharpe are in return space.
    daily = (vx_pnl + es_pnl) / (ES_MULT * demo["ES"].shift(1))
    print(f"APR    {ann_return(daily):.2%}")
    print(f"Sharpe {sharpe(daily):.2f}")
