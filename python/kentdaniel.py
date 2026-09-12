"""Cross-sectional momentum: rank names on 1-year return.

Long the top decile, short the bottom decile, hold ~1 month (overlapping).
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from helpers import ann_return, daily_return, sharpe


def cs_momentum(prices: pd.DataFrame, lookback: int = 252, hold: int = 21) -> pd.Series:
    """`prices` = columns are tickers, rows are dates, values are closes."""
    r = prices.apply(daily_return)
    past = (1 + r).rolling(lookback).apply(np.prod, raw=True) - 1
    past = past.shift(1)

    def long_short(row: pd.Series) -> pd.Series:
        s = row.dropna()
        if len(s) < 10:
            return pd.Series(0.0, index=row.index)
        q_hi, q_lo = s.quantile(0.9), s.quantile(0.1)
        w = pd.Series(0.0, index=row.index)
        longs, shorts = row >= q_hi, row <= q_lo
        n_l, n_s = longs.sum(), shorts.sum()
        if n_l:
            w[longs] = 1.0 / n_l
        if n_s:
            w[shorts] = -1.0 / n_s
        return w

    weights = past.apply(long_short, axis=1)
    # Stagger: average of last `hold` days of target weights.
    pos = weights.rolling(hold).mean()
    pnl = (pos.shift(1) * r).sum(axis=1)
    return pnl


if __name__ == "__main__":
    rng = np.random.default_rng(3)
    idx = pd.bdate_range("2007-01-02", periods=400)
    tickers = list("ABCDEFGHIJ")
    prices = pd.DataFrame(
        100 * np.exp(np.cumsum(rng.normal(0, 0.012, (len(idx), len(tickers))), axis=0)),
        index=idx,
        columns=tickers,
    )
    pnl = cs_momentum(prices)
    print(f"APR    {ann_return(pnl):.2%}")
    print(f"Sharpe {sharpe(pnl):.2f}")
