"""Gold contango: long GLD (spot ETF), short GC (gold futures).

Spot shocks cancel; you keep the roll from being short the future.
"""

from __future__ import annotations

import pandas as pd

from helpers import ann_return, daily_return, sharpe


def spread_returns(gld: pd.Series, gc: pd.Series) -> pd.Series:
    # Dollar-neutral-ish: +1 unit of GLD return, -1 unit of GC return.
    return daily_return(gld) - daily_return(gc)


if __name__ == "__main__":
    # Toy path so the file runs without Chan's .mat files.
    prices = pd.DataFrame(
        {
            "GLD": [160, 160.2, 159.8, 161.0, 160.5],
            "GC": [1610, 1611, 1609, 1618, 1614],
        }
    )
    pnl = spread_returns(prices["GLD"], prices["GC"])
    print("daily spread returns:")
    print(pnl)
    print(f"APR    {ann_return(pnl):.2%}")
    print(f"Sharpe {sharpe(pnl, rf_annual=0.02):.2f}  (vs 2% risk-free)")
