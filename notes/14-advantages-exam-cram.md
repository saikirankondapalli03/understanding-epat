# 14 — Advantages, disadvantages, exam cram

**Slides:** 118–123

← [13 HFT and exits](13-hft-and-exits.md) · [Index](00-READ-IN-THIS-ORDER.md)

---

## Advantages (slides 118–119)

The slide images did not extract as text. From the rest of the lecture, Chan’s case for momentum is:

- Works across **futures, stocks, ETFs, FX** — it is a family, not one ticker trick
- Can have **large capacity** (index futures, broad CS books)
- Trend systems often have **positive skew**: many small losses, occasional large run
- Conceptually **simple** rules (sign of 12-month return; rank and hold a month)
- Can be combined with **short-term reversal** (the CL combo)
- Futures version is often **harvesting roll**, not forecasting news
- You can **choose the cause** (roll vs PEAD vs close rebalance) and match holding period to it

## Disadvantages (slide 120) — write these close to verbatim

1. **Futures momentum often needs a long holding period** → few independent trades → **low Sharpe** and weaker statistical significance.
2. **Event-driven duration shortens** over time (PEAD used to last months; now hours/days). Crowding + faster news.
3. **Momentum crashes** — long underperformance after a financial crisis (file 10). After 1929, drawdown on the order of **30 years**.

## Summary slide — recite this (slides 121–122)

| Cause | What you trade |
|-------|----------------|
| **Futures roll** | TS momentum; CS commodity rank; futures–spot arb (GC–GLD, XLE–USO, **VX–ES**) |
| **Slow news** | Sentiment rank; **PEAD**; other event drifts |
| **Forced flow** | Risk contagion; mutual-fund **Pressure**; index add/delete; **levered-ETF** close |
| **HFT ignition** | Quote matching, ticking, flipping, stop hunting, signed order flow |

## Five calculations to redo on paper

1. Daily return from a close series using a 1-day lag (`mybackshift`).
2. Sign of roll from two points on a forward curve (near vs next).
3. VX–ES: why **long VX is hedged by long ES**, and the `0.1 × DTE` rule.
4. UPRO: given AUM, leverage L, and index return r, dollars to buy/sell at the close: \((L^2 - L) \times r \times \text{AUM}\).
5. PEAD: given overnight return and 90-day σ, long / short / no-trade, exit at close.

## Numbers worth remembering

| Strategy | Headline result |
|----------|-----------------|
| VX–ES roll arb | APR 6.9%, Sharpe 1.0, 1 bp costs |
| TU TS momentum | APR 1.7%, Sharpe 1.0, DD −2.5% (no costs) |
| Other TS futures | Sharpes ~1.05–1.09; VX APR 35% with DD −33% |
| CS stocks | 2007: +37% / 4.1; **2008–09: −30% / −1.3**; 2010–12: +1% / 0.2 |
| DTI index | Sharpe 1.3 into 2008, then **−1.0** in 2009–12 |
| PEAD | APR 6.7%, Sharpe 1.5 (2011–12) |
| UPRO close | APR 32%, Sharpe 2.2 (mid-2011–mid-2012) |
| Pressure factor | ~17% + 17% + 7% sleeves (pre-cost, paper) |

## Pass bar

If you can explain out loud:

1. Why VX–ES **isolates roll**
2. Why **2009** destroyed CS momentum
3. Why UPRO must sell **$32.4M** after a −2% SPX day on $270M AUM

…you understand the lecture. MATLAB is how Chan typed it.

Keep in touch details on the last slide (Chan’s email/blog/site) do not matter for the exam. The workshop reminder is: zip `C:/MomentumWS/` if you were in the live class.
