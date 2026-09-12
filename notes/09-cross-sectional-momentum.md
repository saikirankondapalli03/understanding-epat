# 09 — Cross-sectional momentum

**Slides:** 76–84, 89 (calendar spreads: 80)

← [08 TS rules](08-time-series-trading-rules.md) · Next: [10 Momentum crashes](10-momentum-crashes.md) →

---

## Recap of the difference

TS: did **this** go up?  
CS: did **this beat the others**? Long the top of the rank, short the bottom.

A long–short CS book hedges a lot of **common** movement (market, or “all commodities up together”). What you hope remains is the **difference** — often a difference in **roll** for futures, or a slow **factor** for stocks.

## Physical commodities (slides 76–79)

Claim: spot returns of commodities tend to be **positively correlated**. Then:

- Long the ones with **positive roll**
- Short the ones with **negative roll**

…and net spot partly cancels.

**Practical rule:** every day rank **52** physical commodity futures on **1-year return**. Buy the top, short the bottom, hold a **month**.  
Paper: NBER w20439.

**Results:** pre-crisis looked fine; **2008/1/2–2009/12/31 was poor**. Slide 77 asks why and says “will reveal later.” The reveal is file [10](10-momentum-crashes.md): the short leg bounced.

## Calendar spreads (slide 80)

A **calendar spread** (near vs deferred contract) is almost **pure roll**. If roll persists, **the spread itself trends**. That is another way to harvest cause 1 without taking full outright futures risk.

## S&P 500 stocks (slides 81–84)

Decomposition:

\[
\text{total return} = \text{market} + \text{factor returns} + \text{residual}
\]

Factor returns change **slowly**. A long–short book **hedges market return**.

**Rule (Jegadeesh–Titman / Kent Daniel style):**

- Universe: S&P 500 (can be larger; liquidity is the limit)
- Rank **1-year return** every day
- Long **top decile**, short **bottom decile**
- Hold a **month**

Python: [`python/kentdaniel.py`](../python/kentdaniel.py).

### Numbers to memorize (slide 82)

| Sample | APR | Sharpe |
|--------|-----|--------|
| 2007/5/15–2007/12/31 | 37% | 4.1 |
| 2008/1/02–2009/12/31 | −30% | −1.3 |
| 2010/1/04–2012/04/24 | 1% | 0.2 |

The 2007 window is gorgeous and **short** — do not treat 4.1 as a forecast. The 2008–2009 hole is the real lesson. After that the edge is basically gone in this sample.

## Other ranking factors (slide 89)

Past return / roll is only one sort key. Anything **slow-moving** that separates winners from losers can be a CS factor:

- Fundamental / macro factors (futures)
- Principal component scores
- Earnings growth (stocks)
- Book-to-price (stocks)
- A **linear combination** of the above
- News sentiment (file 11)

---

## Check yourself

1. Why does long–short CS reduce market beta?
2. Why might commodity CS still make money if all commodities are in a bear market?
3. What happened to stock CS in 2008–2009 in this lecture?

Answers: (1) Long and short the same universe. (2) Relative roll / relative strength can still exist. (3) Large negative APR — a **momentum crash**.

Next: [10 Momentum crashes](10-momentum-crashes.md)
