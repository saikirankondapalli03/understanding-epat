"""Lecture: genhurst + vratiotest on TU.

H > 0.5  -> momentum (persistent)
H = 0.5  -> random walk
H < 0.5  -> mean reversion

Variance ratio: var(k-day return) / (k * var(1-day return))
  > 1 -> momentum,  < 1 -> mean reversion.
"""

from __future__ import annotations

import numpy as np
import pandas as pd


def hurst(close: pd.Series, max_lag: int = 100) -> float:
    """Rough Hurst via log-log of RS-like lag variance. Good enough for class."""
    ts = np.log(pd.Series(close, dtype=float).dropna().to_numpy())
    lags = range(2, min(max_lag, len(ts) // 2))
    tau = [np.std(ts[lag:] - ts[:-lag]) for lag in lags]
    slope = np.polyfit(np.log(list(lags)), np.log(tau), 1)[0]
    return float(slope)


def variance_ratio(close: pd.Series, k: int = 10) -> float:
    r1 = pd.Series(close, dtype=float).pct_change().dropna()
    rk = pd.Series(close, dtype=float).pct_change(k).dropna()
    return float(rk.var(ddof=0) / (k * r1.var(ddof=0)))


if __name__ == "__main__":
    rng = np.random.default_rng(5)
    rw = pd.Series(np.exp(np.cumsum(rng.normal(0, 0.01, 2000))))
    print("random-walk-ish  H ~", round(hurst(rw), 3), " (want ~0.5)")
    print("variance ratio k=10:", round(variance_ratio(rw, 10), 3), " (want ~1)")
