# 00b — Study plan: money first, lecture fully covered

Use this **after** [00 — where the money is](00-for-retail-traders.md).  
That file is the verdict. This file is the calendar.

Two tracks run in parallel. Track A is how you might affect dollars. Track B is how you pass/understand Chan. You do **not** turn Track B items into live systems.

← [Money map](00-for-retail-traders.md) · [Index](00-READ-IN-THIS-ORDER.md) · Next: [01 Foundations](01-foundations.md) →

---

## How to use this

- **Track A (explore):** one ETF, one 12-month long-or-flat rule, compare to buy-and-hold, size in dollars. This is the only strategy you *run*.
- **Track B (cover):** every lecture idea, including PEAD, VX–ES, HFT. You must be able to *explain* them. You must not *stack* them onto Track A.

If EPAT/exam is a real deadline, keep Track B dates. If you only care about money, still finish Track B once — otherwise you will wander back into slides looking for a hidden ATM.

**Work product at the end:** a written ticker + rule + crash plan (A), and a one-page “four causes / TS vs CS / why 2009 / why PEAD is crowded” sheet (B).

---

## Strategies: explore vs museum

| Strategy (lecture) | For your money | For the lecture | What “explore” means |
|--------------------|----------------|-----------------|----------------------|
| **12-month TS momentum, long-or-flat, one liquid ETF** | **Explore. This is the book.** | Files 02, 07, 08 | Chart vs buy-and-hold in 2000, 2008, 2022, last bull. Paper or tiny size. 20 logged signals. |
| **Don’t hold contango bleed products** (VXX, many commodity ETPs) | **Explore as avoidance** | Files 05, 06 | List what you will never buy long. Know roll vs spot. |
| Buy-and-hold same ETF (no filter) | **The baseline you must beat or match** | Not in slides | If the filter does not earn its lag, you may just hold. |
| Oil 30d dip + 40d trend combo | Optional later, same family | File 08 / `cl_rev.py` | Only after 20 signals on the simple rule. |
| TU / multi-future pyramid | Literacy; wrong instrument for “2% is my income” | File 08 slide 72 | Know Sharpe ~1 with different APR/DD. Do not clone TU for payoff. |
| VX–ES, GC–GLD, XLE–USO | **Museum as a trade.** Keep the *idea*. | File 06 | Explain: hedge spot, keep roll. Do not build first. |
| CS commodity / S&P deciles | Museum | Files 09, 10 | Explain rank, long–short, 2008–09 crash. |
| PEAD / news sentiment | Museum as a live system | File 11 | Explain slow news; why the gap ate retail leftover. |
| Mutual-fund Pressure, index add/delete, UPRO close | Museum | File 12 | Explain forced flow. Do not day-trade UPRO. |
| HFT flipping / stops / order flow | Museum | File 13 | You are not the hunter. Know exits (time, opposite signal, stop). |

---

## Concepts worth knowing (money) vs concepts you still must cover (lecture)

**Money concepts (go deep until they are boring)**

- Return, long vs short, costs, APR vs Sharpe vs drawdown ([01](01-foundations.md))
- Time-series vs cross-sectional ([02](02-two-types-of-momentum.md)) — you will *use* TS, *not* CS
- Four causes ([03](03-four-causes.md)) — you will *use* persistent trend; others are “why the world moves”
- Spot vs futures vs **roll**, backwardation vs contango ([05](05-futures-and-roll-returns.md))
- Serial correlation as a *yes/no* test, not a career ([07](07-testing-time-series-momentum.md))
- The 12-month / ~1-month hold recipe ([08](08-time-series-trading-rules.md))
- Momentum crashes; shorts after panics ([10](10-momentum-crashes.md))

**Lecture concepts (cover, do not productize)**

- Python lag / `pct_change` ([04](04-python-essentials.md)) — tool if you code; spreadsheet is enough for Track A
- Isolating roll, VX–ES hedge −0.3507, `(VIX−VX)/DTE` ([06](06-isolating-roll-vx-es.md))
- Hurst H>0.5, variance ratio ([07](07-testing-time-series-momentum.md))
- CS ranking, factors, calendar spreads ([09](09-cross-sectional-momentum.md))
- PEAD rule, 0.5σ, sentiment papers ([11](11-news-sentiment-and-pead.md))
- Contagion chain, Pressure, UPRO $32.4M math ([12](12-forced-flows.md))
- Quote matching, flipping, stop hunting, signed volume, exits ([13](13-hft-and-exits.md))
- Advantages, disadvantages, summary table ([14](14-advantages-exam-cram.md))

---

## Phase 1 — Vocabulary + verdict (about 1 sitting)

**Track A work:** Write ticker, surplus-only size, −15% in dollars. Read [00](00-for-retail-traders.md) until the ATM vs filter question is answered.

**Track B files:** [01](01-foundations.md) [02](02-two-types-of-momentum.md) [03](03-four-causes.md)

**You are done with Phase 1 when you can say:**

- Return, long, short, Sharpe, drawdown
- TS = this name vs its past; CS = this name vs the others
- Four causes: roll, slow news, forced flow, HFT ignition
- “I am using trend as a filter on ____ ETF, not hunting PEAD/HFT”

---

## Phase 2 — The only strategy you explore (about 1 week of evenings)

This is the **money** phase. Do not start Phase 3 systems in parallel.

**Track A work (required):**

1. Pick **one** liquid equity (or world) ETF. Gold/commodity only if you accept a different cycle.
2. Define: 12-month total return > 0 → long; else **cash**. Recheck ~monthly. No short.
3. On a chart or sheet, mark where you would have been long vs cash through **2008, 2022, and the last bull**. Optional: 2000 if you have the history.
4. Compare to **always long**. Write two sentences: when the filter helped, when it lagged.
5. Freeze the rule. Log the next signals (paper is fine). Target **20** before changing anything.

**Track B files (support the strategy):** [05](05-futures-and-roll-returns.md) (roll so you do not buy USO/VXX as “the asset”), [08](08-time-series-trading-rules.md), enough of [07](07-testing-time-series-momentum.md) for corr + p-value, [10](10-momentum-crashes.md) **before any short**.

**Optional code:** `python/tu_mom.py` is the same *shape* of rule, not a promise of TU’s 1.7%. A spreadsheet of monthly prices is enough.

**You are done with Phase 2 when you have:** ticker, rule, crash/flat policy, and the vs-buy-and-hold write-up.

---

## Phase 3 — Cover the rest of the lecture without turning it into a business (about 1 week)

Read to **explain**, then close the file. No live orders.

| Session | Files | Must-explain (exam/literacy) | Do **not** do |
|---------|-------|------------------------------|---------------|
| 3a | [04](04-python-essentials.md) | Lag, daily return, 0-based index | Rewrite helpers in a new language |
| 3b | [06](06-isolating-roll-vx-es.md) | Why hedge spot; VX–ES long/long; `(VIX−VX)/DTE`; 0.1×DTE | Trade VX or ES |
| 3c | [07](07-testing-time-series-momentum.md) leftover | Hurst, variance ratio, why non-overlapping windows | Optimize lookback on 20 symbols |
| 3d | [09](09-cross-sectional-momentum.md) | Rank, decile, market-neutral *intent* | Short a decile of stocks |
| 3e | [11](11-news-sentiment-and-pead.md) | PEAD rule; duration shortened; **crowding in the gap, not missing HFT** | MOO every earnings print |
| 3f | [12](12-forced-flows.md) | Contagion chain; UPRO (L²−L)×r×AUM | 15-minute 3× ETF scalps |
| 3g | [13](13-hft-and-exits.md) [14](14-advantages-exam-cram.md) | Four HFT names; four exits; three disadvantages | “Ignite” anything |

**You are done with Phase 3 when** file 14’s summary table and the five paper calculations are recitable, and Track A is still **one** rule.

---

## Suggested calendar

| When | Track A (money) | Track B (lecture) |
|------|-----------------|-------------------|
| Day 1 | Ticker + size + read 00 | 01–03 |
| Days 2–3 | 12-month vs buy-and-hold on *your* ETF | 05, 08, 07 (corr only), 10 |
| Days 4–7 | Freeze rule; start a log | 04, 06, 09 |
| Days 8–10 | Keep logging; no new systems | 11–14 |
| After 20 signals | At most **one** change (lookback **or** stay long-only) | Re-skim 14 if exam |

Cram-only (exam tomorrow): 03, 05, 06, 08 table, 10, 11 PEAD rule, 12 UPRO math, 14. Then return to Track A. Do not “cram” a live PEAD book.

---

## Lecture coverage checklist (nothing skipped)

Tick when you can teach it in 60 seconds:

- [ ] Slides 4–5, 44 — four causes; TS vs CS
- [ ] 6–34 — array lag / return (Python in this repo)
- [ ] 35–43 — total futures return ≈ spot + roll; backwardation / contango
- [ ] 45–61 — isolate roll; VX–ES hedge and basis rule
- [ ] 62–75 — correlation test; TU-style TS rule; other futures Sharpes ~1; CL combo
- [ ] 76–89 — CS futures/stocks; ranking factors; crashes named
- [ ] 90–96 — sentiment; PEAD; other events
- [ ] 97–109 — contagion; Pressure; index; levered ETF math
- [ ] 110–123 — HFT names; exits; pros/cons/summary

Covered ≠ traded.

---

## After this plan

Stay on Track A until it is boring. Deeper *money* work is only: the same ETF, the same rule vs buy-and-hold, costs, and whether you even need the filter. Deeper *lecture* work is file 14 recitation.

Start Phase 1: [01 Foundations](01-foundations.md).
