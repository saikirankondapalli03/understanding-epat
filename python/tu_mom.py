"""Time-series momentum: buy if lookback return > 0, short if < 0.

Hold `hold` days. A new overlapping slice starts every day (pyramid).
Lecture on TU: lookback=250, hold=25 -> APR 1.7%, Sharpe 1.0, DD -2.5%.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from helpers import ann_return, daily_return, max_drawdown, sharpe


def ts_momentum(close: pd.Series, lookback: int = 250, hold: int = 25) -> pd.Series:
    r = daily_return(close)
    # Past lookback-day compounded return, known at yesterday's close.
    past = (1 + r).rolling(lookback).apply(np.prod, raw=True) - 1
    signal = np.sign(past.shift(1))  # +1 long, -1 short, 0 flat
    # Average of the last `hold` daily signals = staggered / pyramided book.
    pos = signal.rolling(hold).mean()
    return pos.shift(1) * r  # trade next day's return


if __name__ == "__main__":
    rng = np.random.default_rng(1)
    close = pd.Series(100 * np.exp(np.cumsum(rng.normal(0.0003, 0.004, 2000))))
    pnl = ts_momentum(close, lookback=250, hold=25)
    print(f"APR    {ann_return(pnl):.2%}")
    print(f"Sharpe {sharpe(pnl):.2f}")
    print(f"MaxDD  {max_drawdown(pnl):.2%}")
