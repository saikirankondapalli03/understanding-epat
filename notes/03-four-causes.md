# 03 — Four causes of momentum

**Slides:** 4–5, 97, 121–122

← [02 Two types](02-two-types-of-momentum.md) · Next: [04 MATLAB essentials](04-matlab-essentials.md) →

---

## Why this file exists

Chan does not treat momentum as a mysterious property of charts. He asks: **what real-world mechanism keeps pushing price the same way?** Each later topic is one mechanism plus the trades that stand in front of it.

If you can point at a strategy and name its cause, you understand the lecture.

## Cause 1 — Persistence of futures roll returns

A futures contract is not the spot asset. Part of its return is **roll**: the contract price sliding toward spot / toward the next maturity, even if spot is unchanged.

If the **shape of the futures curve stays the same for a long time**, roll stays positive or stays negative. That persistent drift **is** time-series momentum in futures.

Full treatment: files [05](05-futures-and-roll-returns.md) and [06](06-isolating-roll-vx-es.md).

## Cause 2 — Slow diffusion, analysis, and acceptance of news

Markets do not instantly agree on what an earnings print or a headline means. Price jumps, then **keeps drifting** in the same direction. The textbook case is **PEAD** (post-earnings-announcement drift), studied since 1968.

Full treatment: file [11](11-news-sentiment-and-pead.md).

## Cause 3 — Forced sales and purchases

Funds sometimes trade because they **must**, not because they learned something about the stock:

- Risk desks cutting leverage after a loss (**contagion**)
- Investor redemptions / subscriptions in mutual funds
- **Index** additions and deletions
- **Levered ETFs** rebalancing at the close

Flow begets more flow. That chain looks like momentum.

Full treatment: file [12](12-forced-flows.md).

## Cause 4 — HFT “momentum ignition”

On very short horizons, order-book tactics can **start** a burst that other traders chase: quote matching, flipping, stop hunting, leaning on order flow.

Full treatment: file [13](13-hft-and-exits.md). This is conceptual (names + economics), not a how-to.

## How the rest of the notes map to these causes

| Cause | Files |
|-------|--------|
| Roll returns | 05, 06, 07, 08, 09 (commodities) |
| Slow news | 11 |
| Forced flow | 12 |
| HFT ignition | 13 |
| Why strategies die | 10 (crashes), 14 (pros/cons) |

---

## Check yourself

Name the cause:

1. UPRO sells $32M of S&P names into a weak close.
2. A stock gaps up on earnings and keeps rising into the close.
3. VIX futures sit cheap vs VIX and grind toward VIX.
4. Stops cluster at 17.00 and a push through them extends the drop.

Answers: (1) forced flow (2) slow news (3) roll (4) HFT ignition.

Next: [04 MATLAB essentials](04-matlab-essentials.md) — skip to [05](05-futures-and-roll-returns.md) if you only need concepts.
