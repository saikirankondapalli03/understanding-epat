# 13 — HFT ignition and exits

**Slides:** 5, 110–117  
**Cause:** short-horizon order-book behavior can **start** a burst of momentum.

← [12 Forced flows](12-forced-flows.md) · Next: [14 Exam cram](14-advantages-exam-cram.md) →

This file is **conceptual**: names, economics, exam language. It is not a recipe to run these tactics.

---

## Ratio trade / quote matching (slide 110)

Sit in front of a **large displayed order**. If that order stays, it is a backstop for your exit. If it cancels, you cancel. Fills in front of size **look like** directional flow and can pull others in.

## Ticking (slides 111–112)

Make the bid and the offer (capture the spread) with a **small directional tilt** in inventory when the tape is one-sided. Spread capture plus a drift if momentum is already there.

## Flipping (slide 113)

Create the **impression** of buying pressure: large buy order at the bid, small sell at the ask. Others buy the ask. Once the sell fills, cancel the bid. The fake bid disappears, others sell the bid, and the short is covered. Mirror image for the other side.

The lecture lists this under **manipulation igniting momentum**.

## Stop hunting (slide 114)

Support/resistance is often a **round number** ($17.00 not $17.15). Stop orders **cluster** there. A push through the level **triggers** those stops; the stops become real selling (or buying) and **extend** the move. Cover after the cascade.

Reference: Osler (2000), “Support for Resistance,” NY Fed.

## Order flow (slides 115–116)

**Signed** volume (buy vs sell) predicts momentum better than **unsigned** volume (just “lots of shares”). Fund flow is another signed series.

If you are not a large market maker or the exchange:

| Market | How you approximate flow |
|--------|---------------------------|
| Futures | Each trade: at the **ask** = + (buy), at the **bid** = − (sell) |
| Stocks | Hard: fragmented lit markets + dark pools, delayed prints |
| FX spot | Often impossible; watch **currency futures** instead |

See also Easley et al. (2012), “Bulk Classification of Trading Activity.”

## Exit strategies (slide 117)

These apply to **all** momentum in the lecture, not only HFT.

| Exit | Logic |
|------|--------|
| **Time-based** | The cause dies on a clock (PEAD / gap / UPRO rebalance → flatten at the close) |
| **New opposite signal** | Return flips from + to − → flip or get out |
| **Stop vs entry** | A loss vs entry **is** “momentum from my price already failed” |
| **Trailing stop** | A loss vs the **recent high** means the run rolled over |

Match the exit to the **cause**. Overnight PEAD with a 12-month trailing stop is a confused strategy.

---

## Check yourself

1. Why is signed volume more useful than raw volume?
2. Why is UPRO flattened at the close, not the next morning?

Answers: (1) Direction of flow, not just activity. (2) The **forced rebalance is a close event**; after the close the cause is gone.

Next: [14 Advantages and exam cram](14-advantages-exam-cram.md)
