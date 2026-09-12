"""When crude is in contango: long XLE, short USO. Flip in backwardation.

`cl_in_contango` is True when the CL forward curve slopes up (near < next).
"""

from __future__ import annotations

import pandas as pd

from helpers import ann_return, daily_return, sharpe


def strategy_returns(
    xle: pd.Series,
    uso: pd.Series,
    cl_in_contango: pd.Series,
) -> pd.Series:
    xle_r = daily_return(xle)
    uso_r = daily_return(uso)
    # +1 = long XLE / short USO; -1 = the reverse.
    # Shift the curve signal by 1 so we do not trade on today's close info.
    pos = cl_in_contango.shift(1).astype("float")
    pos = pos.replace({1.0: 1.0, 0.0: -1.0})
    return pos * (xle_r - uso_r)


if __name__ == "__main__":
    df = pd.DataFrame(
        {
            "XLE": [70, 71, 70.5, 72, 71.5],
            "USO": [30, 31, 30.2, 32, 31.1],
            "cl_in_contango": [True, True, True, False, False],
        }
    )
    pnl = strategy_returns(df["XLE"], df["USO"], df["cl_in_contango"])
    print(pnl)
    print(f"APR    {ann_return(pnl):.2%}")
    print(f"Sharpe {sharpe(pnl):.2f}")
