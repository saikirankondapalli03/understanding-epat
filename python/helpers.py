"""Lag, returns, Sharpe — used by every strategy in this folder."""

from __future__ import annotations

import numpy as np
import pandas as pd


def lag(series: pd.Series | np.ndarray, periods: int = 1) -> pd.Series:
    """Yesterday's value on today's row. First `periods` rows become NaN."""
    s = pd.Series(series)
    return s.shift(periods)


def daily_return(close: pd.Series | np.ndarray) -> pd.Series:
    """(today - yesterday) / yesterday."""
    close = pd.Series(close, dtype=float)
    prev = lag(close, 1)
    return (close - prev) / prev


def moving_average(x: pd.Series | np.ndarray, lookback: int) -> pd.Series:
    """Simple moving average. First lookback-1 rows are NaN."""
    return pd.Series(x, dtype=float).rolling(lookback, min_periods=lookback).mean()


def ann_return(daily: pd.Series, n_days: int = 252) -> float:
    """Compounded annualized return from daily P&L/returns."""
    daily = pd.Series(daily).dropna()
    if daily.empty:
        return float("nan")
    return float((1 + daily).prod() ** (n_days / len(daily)) - 1)


def sharpe(daily: pd.Series, n_days: int = 252, rf_annual: float = 0.0) -> float:
    daily = pd.Series(daily).dropna()
    if daily.std(ddof=0) == 0:
        return float("nan")
    excess = daily - rf_annual / n_days
    return float(np.sqrt(n_days) * excess.mean() / excess.std(ddof=0))


def max_drawdown(daily: pd.Series) -> float:
    equity = (1 + pd.Series(daily).fillna(0)).cumprod()
    peak = equity.cummax()
    dd = equity / peak - 1
    return float(dd.min())
