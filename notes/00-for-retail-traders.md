# 00 — Retail trader: what to focus on (avoid tutorial rot)

**Read this before the lecture notes.** It is for making *decisions*, not collecting files.

← [Index](00-READ-IN-THIS-ORDER.md) · Next: [01 Foundations](01-foundations.md) →

---

## The honest starting point

This lecture will not make you money by itself. It is a map of **why prices sometimes keep going**. Money, if it comes, comes from **one rule you can actually trade**, sized so a crash does not wipe you, after costs.

Tutorial rot is finishing 14 notes, nine Python scripts, and three more courses — and still not having a written rule, a market, and a risk cap.

You beat rot by **narrowing**, not by learning more syntax.

## What a retailer can and cannot do with this lecture

| You can | You probably cannot |
|---------|---------------------|
| Trade **one or two liquid ETFs or futures** with a simple time-series rule | Compete with HFT (flipping, stop hunting, quote matching) |
| Understand **why** a trade should work (roll, news lag, forced flow) | Run a 52-commodity book or a Ravenpack news pipeline |
| Survive by **sizing** for momentum crashes | Trust the lecture Sharpes as live numbers (many ignore costs; samples are old) |
| Hold days to months | Harvest 15-minute levered-ETF rebalance as a career |

If you only have a stock/ETF account: think **ETFs**, not VX–ES contract math. If you have a small futures account: think **one liquid future**, not every symbol on slide 72.

## The three things that actually pay

Everything else in the deck is supporting detail.

### 1. Pick **one cause**, not fourteen indicators

From file 03, momentum has four causes. As a retailer, only two are realistic:

1. **Persistent trend / roll** — “this thing has been going up (or the curve pays longs/shorts) for months.” This is time-series momentum (files 05–08).
2. **Slow news** — a big overnight earnings surprise, hold into the close (file 11). Only if you can get an earnings calendar and live with open slippage.

Skip as a *business*: HFT ignition (file 13), mutual-fund Pressure factors (need CRSP), 52-name commodity CS, NLP sentiment products.

Forced flow (file 12) is useful as **context** (why a dump continues) — not as your first system.

### 2. Prefer **time-series on something cheap to trade**

Cross-sectional “long top decile, short bottom” needs many names, short borrow, and it **died in 2008–2009** (file 10). That is a research strategy.

Retail-friendly version of the lecture:

- One instrument (example: a liquid index or commodity ETF, or TU-like rates future if you have futures).
- Rule: **12-month return positive → long; negative → flat or short** (short only if you understand shorts). Hold ~1 month.
- That is file 08 without the pyramid-of-futures zoo.

Boring is the point. TU in the lecture: **1.7% APR, Sharpe 1.0, drawdown −2.5%**. Not Instagram. Survivable.

### 3. Risk and costs before Python

The lecture’s pretty Sharpes are often **before transaction costs**. Your broker, bid–ask, and missed fills are the real exam.

Write these down **before** you code:

- Max loss per trade (e.g. 0.5–1% of equity)
- Max total drawdown before you stop (e.g. 10–15%)
- What you will do in a **momentum crash**: after a market panic, do **not** blindly stay short yesterday’s dogs (file 10)
- Holding period vs your costs: if you trade daily, costs eat a Sharpe-1 futures rule

If you cannot state those four, more notes will not help.

## What to study in this folder (and what to skip)

**Do, in this order:**

1. This file.
2. [01](01-foundations.md) [02](02-two-types-of-momentum.md) [03](03-four-causes.md) — vocabulary. One evening.
3. [05](05-futures-and-roll-returns.md) — even if you only trade ETFs: you must know roll vs spot or you will confuse “gold went up” with “the curve paid me.”
4. [08](08-time-series-trading-rules.md) — **your first rule**. Read [07](07-testing-time-series-momentum.md) only enough to know “positive correlation + small p-value.”
5. [10](10-momentum-crashes.md) — so you do not blow up the first crisis.

**Skim or skip until you have 20 live (or paper) trades:**

- File 04 and all of `python/` — tools, not the product. Learn `pct_change` and a spreadsheet if that is faster.
- File 06 VX–ES — understand the *idea* (hedge spot, keep roll). Do not build it first.
- File 09 CS stocks — know it exists; do not start here.
- File 11 PEAD — second system, later.
- File 12 UPRO math — know forced buying exists; do not chase the 2011 Sharpe 2.2.
- File 13 HFT — exam/awareness only.
- File 14 — after you can recite the four causes.

## A 30-day plan that is not another tutorial

**Days 1–3.** Finish 01–03 and 05. Write one sentence: *“I will trade ___ because of cause ___.”*

**Days 4–7.** Write the rule on paper (no code required):

```
Market: ________
Lookback: 12 months (or 6 if that is all the history you trust)
Hold: 20 trading days
Long if lookback return > 0, else flat (or short)
Size: $____  so that a 10% adverse move = $____ (must be sleepable)
Costs I assume: $____ round trip
I stop the system if drawdown > ____%
```

**Days 8–14.** Check that rule on **one** chart or a simple spreadsheet / `python/tu_mom.py` idea. You are allowed **one** tweak (lookback or long-only). Then freeze it.

**Days 15–30.** Paper or tiny size. Log every signal: date, why, fill, result. After 20 signals, you may change **one** thing. You may not start PEAD, VX–ES, and oil combo in the same month.

If you skip the log and open another course, that is tutorial rot.

## How you know you are rotting

- You can explain Hurst but cannot state your max dollar loss.
- You rewrote helpers in a third language.
- You added a 13th indicator “just to confirm.”
- You are waiting to understand every slide before the first paper trade.
- You changed markets three times this week.

## How you know you are done *enough* with this lecture

You can say out loud, without notes:

1. Time-series vs cross-sectional.
2. The four causes, and which **one** you are using.
3. Why 2009 wrecked momentum shorts.
4. Your rule, size, and stop.

Then go to [01 Foundations](01-foundations.md) and learn the words. Come back here if you feel the urge to “just finish the Python folder first.”
