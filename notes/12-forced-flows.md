# 12 — Forced sales and purchases

**Slides:** 97–109  
**Cause:** someone **must** trade. Information is optional. Flow creates more flow.

← [11 PEAD](11-news-sentiment-and-pead.md) · Next: [13 HFT and exits](13-hft-and-exits.md) →

---

## Four flavors in this lecture

1. Risk-management **contagion** (levered hedge funds)
2. Mutual-fund **redemptions / subscriptions** (retail herding)
3. **Index** additions and deletions
4. **Levered ETF** rebalancing at the close

## Contagion from constant leverage (slides 98–99)

Memorize the chain:

1. Stock A is a **crowded long** at levered funds.
2. Fund α takes a heavy, possibly **unrelated** loss.
3. α’s risk desk cuts **portfolio size** (constant leverage / Kelly-style).
4. α **sells A**. A falls.
5. Fund β, also long A and similar names, now shows a loss.
6. β’s risk desk deleverages. β sells A.
7. A falls further. **Contagion looks like momentum.**

Same logic for crowded shorts. The key driver: the need to **keep leverage constant after a loss**.

**August 2007** is the case study: Khandani and Lo, “What Happened to the Quants in August 2007?”

Practical problem: hedge-fund holdings **turn over fast** — hard to know the crowded book. **Mutual-fund** holdings are more stable, so they are easier to study (and trade) as a factor.

## Mutual-fund fire sales (slides 100–105)

Same chain, but the “risk desk” is **investors redeeming**:

Fund α loses → investors redeem → α sells crowded stock A → A falls → fund β looks worse → **more** redemptions → β sells A.

Key driver: **herding of retail investors**.

**Critical filter (slide 103):** count buying/selling that is due to **inflows/outflows**, not due to a manager’s stock-specific view. Otherwise you are just copying research, not harvesting forced flow.

### Pressure factor results (slide 104)

Market-neutral, long top-decile Pressure / short bottom, **rebalance quarterly**:

| Sleeve | Idea | Ann. return (pre-cost) |
|--------|------|-------------------------|
| Pressure now | Rank on current flow pressure | **17%** |
| Predicted Pressure | Forecast inflows from **past fund performance** (predict herding) | **another 17%** |
| After 1 quarter | Pressure **mean-reverts** | **another 7%** |

### Liquidity vs fundamentals (slide 105)

- Price moved because someone needed **cash** (redemptions) → often **mean reverts**.
- Price moved because **fundamentals** changed → new level **sticks**.

Holdings data: **CRSP**. The strategy later suffered **crowding** (diminishing returns).

## Index composition (slide 106)

Index funds **must** buy additions and sell deletions. Momentum used to last **multiple days** (Shankar and Miller, 2006, S&P SmallCap 600). Later tests: edge compressed to **intraday**.

## Levered ETFs — do the dollar math (slides 107–109)

A 3× ETF (example **UPRO** on the S&P) must keep

\[
\frac{\text{market value of holdings}}{\text{NAV}} = 3
\]

at the **close**. Down day → they **sell** into weakness. Up day → they **buy** into strength. That is mechanical end-of-day momentum in UPRO **and** in the index names.

### Exercise numbers

UPRO AUM last close ≈ **$270M**. SPX **−2%**.

| Step | Number |
|------|--------|
| Holdings last close | 3 × 270 = **$810M** |
| NAV drop | 2% × 810 = **$16.2M** (also 6% × 270) |
| NAV today | 270 − 16.2 = **$253.8M** |
| Target holdings | 3 × 253.8 = **$761.4M** |
| Holdings before rebalance | 810 − 16.2 = **$793.8M** |
| **Must sell** | 793.8 − 761.4 = **$32.4M** |

Compact formula — dollars to **buy**:

\[
(L^2 - L) \times r \times \text{AUM}
\]

Here \((9 - 3) \times (-0.02) \times 270 = -32.4\) → **sell $32.4M**.

### Their trade

If return from yesterday’s close to **15 minutes before today’s close** is beyond **±2%**, buy/sell UPRO and **exit at the close**.  
APR **32%**, Sharpe **2.2**, mid-2011 to mid-2012.

---

## Check yourself

Redo UPRO with AUM = $270M, L = 3, r = **+2%**. Do they buy or sell, and how much?

Answer: buy **$32.4M** (same magnitude, opposite sign).

Next: [13 HFT and exits](13-hft-and-exits.md)
