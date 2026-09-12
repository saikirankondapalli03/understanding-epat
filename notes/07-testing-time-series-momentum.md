# 07 — Testing time-series momentum

**Slides:** 62–68

← [06 VX–ES](06-isolating-roll-vx-es.md) · Next: [08 TS trading rules](08-time-series-trading-rules.md) →

---

## When you use this

You could not (or did not) hedge spot away. You want to know: **does this future’s own past return predict its future return?** If yes, a trend-follow rule is justified.

## Test A — serial correlation (slides 62–66)

Correlate **lookback** return with later **holding-period** return.

Use **non-overlapping** windows. If you overlap, one crash gets counted twenty times and the p-value lies.

Python: `scipy.stats.pearsonr` gives the correlation **and** a p-value for “true correlation = 0.” See [`python/correlation_test.py`](../python/correlation_test.py).

- Positive correlation + p-value below about **0.05** → evidence of TS momentum.
- You can also correlate the **signs** of past vs future returns (direction persists, not just size). Slide 66 is that table for TU.

### TU (2-year Treasury future) — what the grid says

Instrument: `TU` on CME. Python: [`python/correlation_test.py`](../python/correlation_test.py).

Patterns to remember (not every cell):

- Short holds (1–5 days) are **weak / insignificant**.
- Momentum **shows up** as you lengthen the hold, especially with a **long lookback**.
- Standout cell they later trade: **lookback 250, hold 25** → corr **0.27**, p-value **0.024**.
- Lookback 250 and hold 60: corr **0.42**, p **0.022** — strong, but a 60-day hold means **fewer independent bets** (worse for Sharpe). They pick 25-day hold as the compromise.

**Sign and size of correlations plus small p-values all point to TS momentum in TU** (slide 65).

## Test B — Hurst exponent (slides 67–68)

A single number for “does the series remember its direction?”

| Hurst H | Meaning |
|---------|---------|
| **H > 0.5** | Persistent — **momentum** |
| **H = 0.5** | Random walk |
| **H < 0.5** | Anti-persistent — **mean reversion** |

Function: `hurst()` in [`python/hurst_vratio.py`](../python/hurst_vratio.py).

## Test C — variance ratio

Idea: if daily moves were independent, a 10-day return’s variance would be about **10 ×** one-day variance.

- **Larger** than that → moves cluster in the same direction → momentum.
- **Smaller** → moves cancel → mean reversion.

Python: `variance_ratio()` in [`python/hurst_vratio.py`](../python/hurst_vratio.py). Combined strategy: [`python/tu_mom.py`](../python/tu_mom.py).

---

## Check yourself

1. Why non-overlapping returns?
2. H = 0.62: momentum or reversion?
3. They chose hold = 25, not 60, even though 60 had a bigger correlation. Why is that reasonable?

Answers: (1) Independence / honest p-values. (2) Momentum. (3) More trades per year → usually better Sharpe, still significant.

Next: [08 Time-series trading rules](08-time-series-trading-rules.md)
