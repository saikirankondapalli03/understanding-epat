# 00 — Retail trader: where the money actually is

**Read this before the lecture, and before you “go deeper.”**  
This file is a money map. The other notes are a course. Those are not the same thing.

← [Index](00-READ-IN-THIS-ORDER.md) · Next: [Study plan](00-study-plan.md) →

---

## Verdict (read this twice)

**Most of a retailer’s dollars do not come from Ernest Chan’s 123 slides.** They come from (1) not blowing up, and (2) owning **cheap, liquid risk assets** for years (stock-index ETFs and the like). That risk premium is the pile. Everything in this lecture is a *modifier* of that pile — or a trap.

**The one lecture idea worth going deep on** is **time-series momentum as a filter**: 12-month return up → stay long a liquid ETF; down → go **flat** (cash). You are allowed to go deep *there*. You are not looking for a second salary hiding in Hurst exponents, PEAD, VX–ES, or HFT.

If that verdict feels too small, the lecture will not get bigger. Leverage and vol ETFs only copy the violent rows of slide 72.

## Where retail money actually comes from (ranked)

| Rank | Source of dollars | Is it “this lecture”? | Go deep? |
|-----:|-------------------|------------------------|----------|
| 1 | **Survive.** No 3×, no VXX-as-investment, no size that ruins rent. | Indirect (file 10 crashes, file 05 roll bleed) | **Yes** — this is the cheapest return you will ever earn. |
| 2 | **Asset risk premium.** Being long a broad equity (or similar) ETF through years. Historically this dwarfs timing tricks on $10k. | No. Buy-and-hold is not in the slide deck. | **Yes**, on *which* boring ETF and *what you can stand to lose*. Not on 14 indicators. |
| 3 | **12-month long-or-flat overlay** on that same ETF. | Yes — time-series momentum (files 02, 07, 08). | **Yes, this is the one strategy depth.** You are learning *when to sit in cash*, not a secret 30% engine. In bulls you will look like the index. In some bears you may lose less. In melt-ups after you went flat you will **lag**. |
| 4 | **Don’t pay structural bleed.** Long contango products (many VIX and some commodity ETPs) leaks roll every month. | Yes — files 05–06, as *avoidance*. | **Yes, conceptually.** You do not need to *trade* GC vs GLD. You need to stop holding the bleeding thing. |
| 5 | Everything else in the deck (PEAD, CS ranks, UPRO close, VX–ES, HFT, news NLP). | Yes, as exam/history. | **No as a business.** Depth here is tutorial rot unless you already have (3) running and logged. |

**Chan’s TU 1.7% APR is not your payoff.** TU is a sleepy 2-year rate future. Same *rule* on a stock or commodity index has **stock-like or commodity-like** years (often roughly **6–12%** in a decent decade on equities, with **−20% to −40%** still possible if you are long before the signal flips). Same rule on vol can print **30%+** and then **−30% or ~$0**. You choose the asset’s pain, not a free upgrade.

On **$10k**, a non-ridiculous year on an equity ETF overlay is **hundreds to about a thousand**, lumpy, not ~$80 every month. A bad stretch is **−$1,500 to −$2,500** or worse. If that cannot matter in your life, you need **more capital or a job**, not a deeper lecture.

## What “going deep” should mean (and what it must not)

**Worth depth — this is where leftover lecture-money lives for you**

1. **One liquid ETF** you can buy cheaply (broad equity is the default; gold/commodity only if you accept different cycles).
2. **The 12-month rule vs buy-and-hold** on *that* chart: 2000, 2008, 2022, and the last bull. If the filter never earned its lag, you may just hold the ETF. That comparison *is* the research.
3. **Roll** enough to know why USO ≠ oil spot and VXX is not a long-term long (file 05).
4. **Crashes** (file 10): long-or-flat first; shorts after panics are how momentum books die.
5. **Costs, taxes, size:** monthly vs yearly rebalance; max drawdown in *dollars*; surplus cash only (emergency fund stays out).

**Not where the money is — looks like depth**

- PEAD / earnings drift: you *can* place the trade without HFT. Funds already took the overnight gap. Open slippage eats the leftover. Cause to understand; not a system ([file 11](11-news-sentiment-and-pead.md)).
- Cross-sectional top/bottom decile: needs many names and shorts; wrecked in 2008–09; lecture’s later Sharpe ~0.2.
- VX–ES, GC–GLD as a *book*: right idea (isolate roll), wrong first business (contracts, ops).
- UPRO 15-minute close: 2011–12 sample, crowded, day-trade rules.
- HFT ignition: you are the prey, not the hunter.
- Python/MATLAB fluency as a goal: a spreadsheet can run 12-month vs price. Code after the rule is frozen.

## What you can and cannot do with this lecture

| You can | You probably cannot |
|---------|---------------------|
| Overlay **one or two liquid ETFs** with a monthly time-series rule | Compete with HFT |
| Use roll knowledge to **avoid** bleed products | Clone a 52-commodity or 500-stock long–short |
| Cut risk when the 12-month trend is down | Turn $10k into a salary |
| Treat 2012 Sharpes as **history**, not a quote | Harvest PEAD or levered-ETF closes as a career |

Stock/ETF account → ETFs. Small futures account → still **one** liquid contract, not slide 72’s whole list. Micros exist now; **$100–$10k** still does not safely margin them the way the slides implied.

## The rule (only one, until it is boring)

```
Market: one cheap, liquid ETF (write the ticker)
Lookback: 12 months
Hold: about 20 trading days, then recheck
If lookback return > 0 → long
If lookback return ≤ 0 → cash (flat). No short until you have lived through a crash on paper.
Size: $____ such that −15% on this sleeve does not change rent
I stop adding complexity until I have 20 logged signals
```

That is file 08, stripped. Going deeper = testing **this** vs buy-and-hold, not adding a 13th indicator.

## What to read next in this folder

**Do, because it supports the verdict:**

1. This file (again, after a night).
2. [01](01-foundations.md) [02](02-two-types-of-momentum.md) [03](03-four-causes.md) — words only.
3. [05](05-futures-and-roll-returns.md) — so you do not confuse spot with roll.
4. [08](08-time-series-trading-rules.md) + enough of [07](07-testing-time-series-momentum.md) to know “positive correlation, small p-value.”
5. [10](10-momentum-crashes.md) — mandatory before any short.

**Skim:** 04/`python/`, 06, 09, 11, 12, 13, 14 — so you can *reject* them on purpose, not because you never saw them.

## Before you go deeper: three questions

If you cannot answer these, more notes will not find hidden money:

1. **Is my pile the ETF’s risk premium, with a filter — or do I think Chan found a separate ATM?** (Only the first is real.)
2. **On my ticker, did 12-month long-or-flat beat buy-and-hold after costs in the last two crashes and the last bull — or did it just feel smarter?**
3. **Can I fund this with surplus, take a −15% year, and not touch it for 20 signals?**

If (1) is “separate ATM,” stop. The money is not there. If (2) is “I have not looked,” that comparison **is** the deep work — a chart or a simple sheet, not another course. If (3) is no, save until the sleeve is $5k–$10k+ or keep it as tuition and expect **~$0** after friction.

## Rot vs done

**Rot:** Hurst without a dollar stop; a third language; PEAD + oil combo + VX in the same month; waiting to finish every slide before one paper month.

**Done enough:** You can say: TS vs CS; the four causes and that you are using **trend as a filter**; why 2009 wrecked shorts; your ticker, size, and stop; and that **the market’s return is the money, the filter is optional insurance.**

Then [Study plan](00-study-plan.md) for the calendar, then [01 Foundations](01-foundations.md) for vocabulary. Come back here when a slide starts to feel like a new business.
