"""PEAD: trade overnight earnings surprise, exit at the close.

    retC2O >  +0.5 * sigma  -> buy at open, sell at close
    retC2O <  -0.5 * sigma  -> short at open, cover at close
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from helpers import ann_return, sharpe


def pead_intraday(
    open_: pd.DataFrame,
    close: pd.DataFrame,
    earnann: pd.DataFrame,
    z: float = 0.5,
    sigma_window: int = 90,
) -> pd.Series:
    """
    All three frames: rows = dates, columns = tickers.
    earnann is 1 if earnings arrived after yesterday's close and before today's open.
    """
    prev_close = close.shift(1)
    ret_c2o = open_ / prev_close - 1
    sigma = ret_c2o.rolling(sigma_window).std()
    ret_intraday = close / open_ - 1  # open-to-close, the hold

    surprise = ret_c2o / sigma
    pos = pd.DataFrame(0.0, index=close.index, columns=close.columns)
    announced = earnann.fillna(0).astype(bool)
    pos[(announced) & (surprise > z)] = 1.0
    pos[(announced) & (surprise < -z)] = -1.0

    n = pos.abs().sum(axis=1).replace(0, np.nan)
    pnl = (pos * ret_intraday).sum(axis=1) / n
    return pnl.fillna(0.0)


if __name__ == "__main__":
    rng = np.random.default_rng(4)
    idx = pd.bdate_range("2011-01-03", periods=80)
    tickers = ["AAA", "BBB", "CCC"]
    close = pd.DataFrame(
        50 * np.exp(np.cumsum(rng.normal(0, 0.01, (len(idx), 3)), axis=0)),
        index=idx,
        columns=tickers,
    )
    open_ = close.shift(1) * (1 + rng.normal(0, 0.005, close.shape))
    earnann = pd.DataFrame(rng.random(close.shape) < 0.05, index=idx, columns=tickers)
    pnl = pead_intraday(open_, close, earnann)
    print(f"APR    {ann_return(pnl):.2%}")
    print(f"Sharpe {sharpe(pnl):.2f}")
