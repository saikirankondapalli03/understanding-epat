# 11 — News sentiment and PEAD

**Slides:** 90–96  
**Cause:** slow diffusion, analysis, and acceptance of information.

← [10 Crashes](10-momentum-crashes.md) · Next: [12 Forced flows](12-forced-flows.md) →

---

## Why prices drift after news

If every trader instantly agreed on the meaning of an announcement, you would see **one jump** and then a flat line. In reality:

- Not everyone sees it at once
- Not everyone agrees what it implies
- Models and humans update with a lag

So price **jumps, then keeps going the same way**. That leftover is event-driven momentum.

## News sentiment as a ranking factor (slides 90–91)

NLP reads the news feed, assigns a **sentiment score** (expected price impact) to each story, then **aggregates** scores over a window.

**Strategy:** long–short portfolio ranked on that aggregated score.

Ravenpack study cited: APR **52% to 156%**, Sharpe **3.9 to 5.3** *before* transaction costs. Treat the magnitude as “it worked in their sample,” not as a live expectation. The **economic** point: success of sentiment ranking is evidence for **slow diffusion** (cause 2).

You can also skip blended sentiment and measure **each event type** separately.

## PEAD — post-earnings-announcement drift (slides 92–94)

Known since **1968**. Review: Bernard and Thomas, 1989, *Journal of Accounting Research*. Still profitable in Chan’s 2011–2012 window. **Duration has shortened** over the years (hours/days instead of months).

### The rule

Universe: S&P stocks. Flag: earnings announced **after yesterday’s close and before today’s open** (`earnann == 1`).

Let `retC2O` = close-to-open return (the overnight gap). Compare it to how wild those gaps usually are: **90-day standard deviation** of `retC2O`.

| Signal | Action |
|--------|--------|
| `retC2O > +0.5 × σ` | **Buy** at the open |
| `retC2O < −0.5 × σ` | **Short** at the open |
| otherwise | No trade |
| Exit | **Market close** (intraday). Exercise: also try holding overnight |

Data: stock OHLC file + `earnannfile`. Program: `pead.m`.

**Results (2011/1/3–2012/4/24, SPX stocks):** APR **6.7%**, Sharpe **1.5**.

## Other events (slides 95–96)

Same template, different trigger:

- Earnings guidance
- Analyst rating / recommendation changes
- Same-store sales
- Airline load factors
- M&A announcements
- Macro data and interest-rate announcements (ETFs / futures / FX)

Hafez (2011), Ravenpack “Event Trading Using Market Response”: a surprise vs street intuition — after M&A, the **acquiree** can fall **more** than the acquirer. Measure, do not assume.

Some drifts last **minutes**. Example: BOE rate announcement → GBPUSD momentum for about **10 minutes** (Clare and Courtnenay, 2001).

---

## Check yourself

1. Why exit PEAD at the close in this lecture?
2. What does 0.5 × 90-day σ do?
3. Name the cause of momentum this whole file sits under.

Answers: (1) They are harvesting **same-day** drift after the overnight surprise. (2) Require a **large** surprise vs that stock’s own overnight noise. (3) Slow diffusion of news.

Next: [12 Forced flows](12-forced-flows.md)
