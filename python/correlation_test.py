"""Non-overlapping lookback return vs later holding-period return.

Positive correlation + small p-value => time-series momentum.
Lecture standout on TU: lookback=250, hold=25 -> corr 0.27, p=0.024.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
from scipy.stats import pearsonr

from helpers import daily_return


def nonoverlapping_pairs(
    close: pd.Series,
    lookback: int,
    hold: int,
) -> tuple[np.ndarray, np.ndarray]:
    r = daily_return(close).fillna(0)
    past, future = [], []
    i = lookback
    while i + hold <= len(r):
        past.append(float((1 + r.iloc[i - lookback : i]).prod() - 1))
        future.append(float((1 + r.iloc[i : i + hold]).prod() - 1))
        i += hold  # jump by hold so windows do not overlap
    return np.array(past), np.array(future)


def corr_pvalue(close: pd.Series, lookback: int, hold: int) -> tuple[float, float]:
    past, future = nonoverlapping_pairs(close, lookback, hold)
    if len(past) < 3:
        return float("nan"), float("nan")
    r, p = pearsonr(past, future)
    return float(r), float(p)


def grid(close: pd.Series, lookbacks=(25, 60, 120, 250), holds=(1, 5, 10, 25, 60, 120, 250)):
    rows = []
    for L in lookbacks:
        for H in holds:
            r, p = corr_pvalue(close, L, H)
            rows.append({"lookback": L, "hold": H, "corr": r, "p_value": p})
    return pd.DataFrame(rows)


if __name__ == "__main__":
    rng = np.random.default_rng(0)
    # Mild momentum toy series (not the lecture's TU).
    noise = rng.normal(0, 0.003, 1500)
    close = pd.Series(100 * np.exp(np.cumsum(noise + 0.0002 * np.sign(noise))))
    print(grid(close).round(4).to_string(index=False))
