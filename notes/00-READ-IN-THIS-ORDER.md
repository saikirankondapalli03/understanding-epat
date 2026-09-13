# Quantitative Momentum Strategies — study path

Ernest Chan, EPAT lecture (123 slides).  
Source PDF: `EFS-04-05Quantitative-Momentum-StrategiesLN.pdf`

**Start here if you want to trade, not collect notes:** [00-for-retail-traders.md](00-for-retail-traders.md) (where the dollars are), then [00-study-plan.md](00-study-plan.md) (calendar: money track + full lecture coverage). Then the numbered files. Do not skip to VX–ES or PEAD until roll returns make sense.

Chan wrote MATLAB. All code in these notes is **Python**; runnable copies live in [`python/`](../python/README.md).

| Order | File | What it unlocks | Slides |
|------:|------|-----------------|--------|
| 0 | [00-for-retail-traders.md](00-for-retail-traders.md) | Where retail dollars actually are; what is worth going deep on | — |
| 0b | [00-study-plan.md](00-study-plan.md) | Money-first calendar that still covers every lecture block | — |
| 1 | [01-foundations.md](01-foundations.md) | Price, return, long/short, backtest language | — |
| 2 | [02-two-types-of-momentum.md](02-two-types-of-momentum.md) | Time-series vs cross-sectional | 44 |
| 3 | [03-four-causes.md](03-four-causes.md) | The map of the whole lecture | 4–5, 121–122 |
| 4 | [04-python-essentials.md](04-python-essentials.md) | Arrays, lag, returns in Python | 6–34 |
| 5 | [05-futures-and-roll-returns.md](05-futures-and-roll-returns.md) | Spot vs futures, contango, backwardation | 35–43 |
| 6 | [06-isolating-roll-vx-es.md](06-isolating-roll-vx-es.md) | Hedge spot, keep roll; VX–ES | 45–61 |
| 7 | [07-testing-time-series-momentum.md](07-testing-time-series-momentum.md) | Correlation, Hurst, variance ratio | 62–68 |
| 8 | [08-time-series-trading-rules.md](08-time-series-trading-rules.md) | TU and other futures trend rules | 69–75 |
| 9 | [09-cross-sectional-momentum.md](09-cross-sectional-momentum.md) | Rank, long winners, short losers | 76–84, 89 |
| 10 | [10-momentum-crashes.md](10-momentum-crashes.md) | Why 2008–2009 destroyed the book | 77, 85–88 |
| 11 | [11-news-sentiment-and-pead.md](11-news-sentiment-and-pead.md) | Slow diffusion of news | 90–96 |
| 12 | [12-forced-flows.md](12-forced-flows.md) | Contagion, index, levered ETFs | 97–109 |
| 13 | [13-hft-and-exits.md](13-hft-and-exits.md) | Microstructure ignition + how to exit | 110–117 |
| 14 | [14-advantages-exam-cram.md](14-advantages-exam-cram.md) | Pros/cons and what to recite | 118–123 |

## One-day timing

- File 00 (money map): 20 minutes. Decide filter vs fantasy ATM.
- File 00b (study plan): 15 minutes. Mark explore vs museum.
- Files 01–03: 45 minutes (do not rush the vocabulary).
- File 04: 60 minutes if you must code (Python in `python/`); 20 minutes if the exam is conceptual.
- Files 05–06: 2 hours (this is the hard core).
- Files 07–10: 2 hours.
- Files 11–14: 90 minutes.

**Money vs exam:** if you only have one day to *trade*, do 00 + 00b + 05 + 08 + 10 and start the ETF vs buy-and-hold sheet. If you have an exam, also finish **06, 11 (PEAD rule), 12 (UPRO math), 14**. Covered ≠ traded. See [00-study-plan.md](00-study-plan.md).
