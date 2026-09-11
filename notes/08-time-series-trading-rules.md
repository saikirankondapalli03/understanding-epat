# 08 — Time-series trading rules

**Slides:** 69–75

← [07 Testing](07-testing-time-series-momentum.md) · Next: [09 Cross-sectional](09-cross-sectional-momentum.md) →

---

## From a test to a trade (TU)

Tests liked **lookback 250, hold 25** (corr 0.27, p = 0.024). Holding period is short enough to still get a decent Sharpe.

**Rule:**

- 12-month return **positive** → **buy** TU  
- 12-month return **negative** → **short** TU  
- Hold about **one month**
- Start a **new overlapping position every day** (“staggered” / “pyramided”). You always have about 25 slices on, so you are not betting on one calendar day.

Program: `TU_mom.m`.

**Results (no transaction costs):** APR **1.7%**, Sharpe **1.0**, max drawdown **−2.5%**. Quiet, stable, not exciting — and that is the point for a rates future.

## Same idea, other futures (slide 72)

| Symbol | Lookback | Hold | APR | Sharpe | Max DD |
|--------|----------|------|-----|--------|--------|
| VX (CFE) | 50 | 5 | 35.2% | 1.09 | −33.2% |
| BR (CME) | 100 | 10 | 17.7% | 1.09 | −14.8% |
| HG (CME) | 40 | 40 | 18.0% | 1.05 | −24.0% |
| TU (CBOT) | 250 | 25 | 1.7% | 1.04 | −2.5% |

Read this table as: **Sharpes huddle near 1.0–1.1.** VX is high-octane (huge return, huge pain). TU is the opposite. Do not pick a strategy on APR alone.

## Indicators — different clothes, same idea (slide 73)

Anything that says “it has been going up”:

- Sign of lagged returns (or of roll)
- New N-day high
- Price above MA or EMA
- Price above upper Bollinger band
- More up-days than down-days
- **Alexander filter:** buy after a move up of at least x%; reverse after a move down of at least x% from the subsequent high

## Best combo: long-term momentum + short-term reversal (slides 74–75)

Do not run pure breakout if a short-term **dip** inside a still-alive uptrend is the better entry.

**CL (crude) exercise:**

- **Buy** at close if price is **lower than 30 days ago** (recent dip) **but higher than 40 days ago** (higher-timeframe uptrend still on).
- Short is the mirror.
- Data: `inputDataOHLCDaily_20120504.mat`. Program: `CL_rev.m`.
- Backtest **momentum alone**, **reversal alone**, and **combo**. Plot all three on one axis with `dateaxis` to see **when** each worked.

The lecture’s claim: combo beats either piece.

---

## Check yourself

1. What does “pyramided every day” mean for a 25-day hold?
2. Why can VX and TU have the same Sharpe and feel nothing alike?
3. In the CL rule, which window is momentum and which is reversal?

Answers: (1) 25 overlapping slices, one entered each day. (2) Volatility / drawdown scale. (3) 40-day = momentum, 30-day = reversal.

Next: [09 Cross-sectional momentum](09-cross-sectional-momentum.md)
