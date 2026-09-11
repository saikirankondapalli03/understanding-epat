# 06 — Isolating roll (pairs and VX–ES)

**Slides:** 45–61

← [05 Futures and roll](05-futures-and-roll-returns.md) · Next: [07 Testing TS momentum](07-testing-time-series-momentum.md) →

---

## The idea

Spot is noisy. Roll can be slow and stubborn. If you can **long something that tracks spot** and **short the future** (or the reverse), spot shocks hit both legs and **cancel**. What remains is mostly roll.

That is why Chan pairs instruments instead of always riding a naked future.

## When there is a traded underlying

**GC vs GLD (slide 46).** Gold futures are usually in **contango**. Trade: **short GC, long GLD** (gold ETF ≈ spot). Exercise: annualized return and Sharpe vs a 2% risk-free rate. Data: `inputData_GC_…mat`, ETF file. Program: `GLD_GC.m`.

## When there is no clean underlying (slide 47)

Pair the future with anything **highly correlated (or anti-correlated)** with its **spot** return: another future, an ETF, an FX future, even ETF vs ETF.

Examples to invent in an interview: CL vs USO, ES vs SPY, rates futures vs TLT, VX vs ES.

## XLE vs USO (slides 48–49)

Crude (CL) in **contango** → long energy stocks **XLE**, short oil ETF **USO** (and the reverse in backwardation). You are using two ETFs to harvest CL’s roll. Program: `XLE_CL_rollReturn.m`. Data: daily CL + ETF file.

## VX–ES — the worked example you must reproduce

### Why this pair is special (slide 50)

- VX (VIX futures) has **huge** roll, on the order of **50% annualized**.
- VIX (spot vol) is strongly **anti-correlated** with ES (S&P future): daily-return correlation about **−75%**.
- ES itself has **little roll**.

So a hedged VX–ES book should capture **much of VX’s roll** and throw away the “stocks ripped / vol crushed” shock.

### Align the series and look (slides 51–54)

```matlab
idxV = find(strcmp('VX', syms));
idxE = find(strcmp('ES', syms));
% intersect dates, then:
scatter(VX, ES);
```

**Two regimes.** After the 2008 crisis: **lower VX for the same ES**, but **more extreme** vol spikes. Fit the hedge only on **post-August 2008** data.

### Hedge in dollars (slide 55)

Contract multipliers: ES **$50 per point**, VX **$1000 per vol point**.

```matlab
post200808 = find(tday >= 20080801);
hedgeRatio = regress(50 * ES(post200808), ...
    [1000 * VX(post200808) ones(length(post200808), 1)]);
% hedgeRatio(1) = -0.3507
```

Negative beta: VX and ES move opposite. **Long VX is hedged by long ES** (short VX by short ES). You are cancelling the equity-vol shock, not doubling it.

### Do not fit a straight line to the whole VX curve (slides 57–59)

The **log forward curve of VX is not a straight line**, so OLS-on-all-maturities is a bad roll estimate (that method was more reasonable for something like corn). Use the **front contract vs spot VIX**:

\[
\text{roll} \approx \frac{\text{VIX} - \text{VX}}{\text{trading days to settlement}}
\]

### The actual rule (slides 59–60)

Hold **one day**. Threshold: `0.1 × number of trading days until settlement`.

| Condition | Trade |
|-----------|--------|
| VIX − VX > 0.1 × DTE (future cheap → expected +roll) | Buy **0.3507 VX** and buy **1 ES** |
| VX − VIX > 0.1 × DTE (future rich → expected −roll) | Short **0.3507 VX** and short **1 ES** |

Code is messy only because you need each front contract’s **settlement date** (`VX_ES_rollreturn.m`).

**Results:** APR **6.9%**, Sharpe **1.0**, t-cost **1 bp**.  
Paper: Simon and Campasano, 2012, “The VIX Futures Basis.”

## When no pair exists (slide 61)

Happy anti-correlated pairs are rare. Plan B: if **long-term spot is uncorrelated or smaller than roll**, a **naked** time-series momentum rule on the future can still work. That is files 07–08. You must **test** first.

---

## Check yourself

1. Why is long VX hedged by **long** ES, not short ES?
2. Why not use one slope from the entire VX forward curve?
3. What does the 0.1 × DTE filter do?

Answers: (1) They move **opposite** — same-side positions offset the shock. (2) Curve is **not linear**. (3) Trade only when the basis is **wide enough** vs time left.

Next: [07 Testing time-series momentum](07-testing-time-series-momentum.md)
