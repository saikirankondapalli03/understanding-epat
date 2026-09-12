# 05 — Futures and roll returns

**Slides:** 35–43

← [04 Python](04-python-essentials.md) · Next: [06 Isolating roll / VX–ES](06-isolating-roll-vx-es.md) →

This is the hard core of the lecture. Do not leave until the gold example is obvious.

---

## Spot is not the future

**Spot** = the thing now (gold in a vault, oil for delivery, the S&P index).

**Futures** = a contract to buy or sell that thing on a **later date**. At expiry the futures price **must meet** spot. Until then they can differ.

You can make or lose money in the future **even if spot does not move**. That extra piece is **roll return**.

\[
\text{total futures return} \approx \text{spot return} + \text{roll return}
\]

## Forward curve (term structure)

Fix **one date in history**. Plot each contract’s price against **time to maturity**. That snapshot is the **forward curve**.

It is not a chart of price evolving through time. It is “what the market charges today for delivery in 1 month, 3 months, 12 months.”

## Backwardation — positive roll

Near contract is **richer** (higher price) than later contracts. Curve slopes **down**.

If that shape **persists**, a long futures position is sitting in a contract that, as it ages, lives in a cheaper part of the old curve — it tends to **roll up** toward the higher front / toward spot. Longs **earn** roll.

Everyday picture: the barrel you can have *soon* is scarce, so people pay up for it.

## Contango — negative roll

Near contract is **cheaper** than later contracts. Curve slopes **up**.

If that shape persists, a long position **rolls down**. Longs **bleed** roll. Gold (GC) is often in this camp.

### Tiny example

- Spot gold = 2000
- 1-month future = 2010
- 12-month future = 2120 → **contango**

If this shape stays, the 12-month contract is above where it must eventually go. As months pass it is pulled down toward ~2000. A long loses that gap. That loss is **negative roll**, not “gold went down.”

## How to estimate spot vs roll (slides 39–43)

You do not need a fancy model for the exam. Two practical views:

1. **Two points on the curve.** If \(F_{\text{near}} > F_{\text{next}}\) → backwardation (positive roll for the long). If \(F_{\text{near}} < F_{\text{next}}\) → contango (negative roll). Annualize by dividing by the time between those maturities.

2. **Regression snapshot.** At one date, regress log futures prices on time to maturity. Intercept is in the neighborhood of log spot; **slope is roll**. Then watch how intercept vs slope **change through time**: that splits “spot moved” from “curve paid you.”

Chan’s empirical punchline (the missing chart on slide 43): **roll is often more persistent / more tradable than spot.** Spot wiggles; the curve’s sign can sit still for a long time. That persistence is why futures **trend**.

## Sketch you should be able to draw (slide 38)

- Backwardation: price on the vertical axis, time-to-maturity on the horizontal; a **downward** line.
- Contango: an **upward** line.

---

## Check yourself

1. Spot unchanged, you are long a contango contract, curve shape unchanged. Do you expect to make or lose money?
2. Why can futures momentum exist even if you have **no view** on whether oil will go up?

Answers: (1) Lose — negative roll. (2) Because **roll** can keep the same sign for a long time.

Next: [06 Isolating roll / VX–ES](06-isolating-roll-vx-es.md)
