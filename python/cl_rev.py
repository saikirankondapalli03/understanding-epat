"""Crude: long-term momentum plus short-term reversal.

Buy if price is below 30 days ago (dip) but above 40 days ago (uptrend).
Short is the mirror. Combo should beat either rule alone.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from helpers import ann_return, daily_return, lag, sharpe


def combo_signal(close: pd.Series, short: int = 30, long: int = 40) -> pd.Series:
    px = pd.Series(close, dtype=float)
    vs_short = px - lag(px, short)  # negative = dip vs 30d ago
    vs_long = px - lag(px, long)    # positive = still above 40d ago
    long_sig = (vs_short < 0) & (vs_long > 0)
    short_sig = (vs_short > 0) & (vs_long < 0)
    pos = pd.Series(0.0, index=px.index)
    pos[long_sig] = 1.0
    pos[short_sig] = -1.0
    return pos


def momentum_only(close: pd.Series, long: int = 40) -> pd.Series:
    px = pd.Series(close, dtype=float)
    return np.sign(px - lag(px, long))


def reversal_only(close: pd.Series, short: int = 30) -> pd.Series:
    px = pd.Series(close, dtype=float)
    return -np.sign(px - lag(px, short))  # fade the 30-day move


def backtest(close: pd.Series, pos: pd.Series) -> pd.Series:
    return pos.shift(1) * daily_return(close)


if __name__ == "__main__":
    rng = np.random.default_rng(2)
    close = pd.Series(80 * np.exp(np.cumsum(rng.normal(0, 0.015, 800))))
    for name, pos in [
        ("momentum", momentum_only(close)),
        ("reversal", reversal_only(close)),
        ("combo", combo_signal(close)),
    ]:
        pnl = backtest(close, pos)
        print(f"{name:10} APR {ann_return(pnl):7.2%}  Sharpe {sharpe(pnl):5.2f}")
