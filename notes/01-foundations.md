# 01 — Foundations

**Read this first.** Every later file uses these words.

← [Index](00-READ-IN-THIS-ORDER.md) · Next: [02 Two types of momentum](02-two-types-of-momentum.md) →

---

## Price

The last traded value of an instrument. In the lecture, daily **close** is the usual price.

## Return

How much you made, as a fraction of what you put on.

If you buy at 100 and sell at 110:

\[
\text{return} = \frac{110 - 100}{100} = +10\%
\]

If it falls to 90, the return is \(-10\%\).

A **daily return** is that calculation from yesterday’s close to today’s close. In Python you **lag** the close (yesterday’s price on today’s row), then `(today - yesterday) / yesterday`. That is `lag` / `pct_change` in file 04 and `python/helpers.py`.

## Long and short

- **Long:** you own it (or a contract that pays if it rises). You profit if price goes **up**.
- **Short:** you borrowed it and sold it. You must buy it back later. You profit if price goes **down**.

A strategy is always choosing: long, short, or nothing (**flat**).

## P&L, APR, Sharpe, drawdown

These are how Chan scores a backtest.

| Term | Meaning |
|------|---------|
| P&L | Profit and loss in currency |
| APR | Annualized return — roughly “how much per year” |
| Sharpe ratio | Return divided by how bumpy the returns were. Near **1.0** is typical for the futures trend rules in this lecture |
| Max drawdown | Worst peak-to-trough loss on the equity curve |

Sharpe matters more than raw APR for comparing strategies. VX in later files has a huge APR and a huge drawdown; TU has a tiny APR and a tiny drawdown. Their Sharpes are almost the same.

## Backtest

Run a rule on **old** prices as if you had traded it, then measure APR / Sharpe / drawdown. It is not a guarantee of the future. Chan still uses it as the standard way to show “this cause of momentum was harvestable in sample.”

## Transaction costs (t-cost)

Fees plus bid–ask slippage. Some results in the lecture ignore costs; VX–ES quotes **1 basis point** (0.01%). If two strategies have similar Sharpe before costs, the one that trades less often usually wins after costs.

---

## Check yourself

1. You buy at 50, sell at 45. Return? Long or short would have won?
2. Why might a 35% APR strategy be worse to live with than a 2% APR strategy?

Answers: (1) \(-10\%\); a **short** would have won. (2) Drawdown / volatility — look at Sharpe, not only APR.

Next: [02 Two types of momentum](02-two-types-of-momentum.md)
