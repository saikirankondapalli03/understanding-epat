# 03 — Four questions, four ratio families

Ratios exist because a raw number has no plot.

← [02 What the business owns and owes](02-what-the-business-owns-and-owes.md) · Next: [04 Industry fingerprints](04-industry-fingerprints.md) →

---

## In one sentence

Every useful ratio in Chapter 1 answers one of four questions: can it pay its bills soon, does it make money, how did it fund itself, and how hard do its assets work?

---

## Why divide one number by another

“Coca-Cola earned billions.” Is that a lot? You cannot know.

“Coca-Cola kept about 16 cents of every sales dollar.” Now you know something. You can compare that 16% to last year, to Pepsi, and to a grocer who is lucky to keep 3 cents.

Desai’s four questions:

1. **Liquidity** — can this firm survive the next year without running out of cash?
2. **Profitability** — does the business keep money, and what do owners earn on their stake?
3. **Financing / leverage** — how much of the firm is other people’s money?
4. **Productivity / efficiency** — how much activity is squeezed out of the asset pile?

---

## 1. Liquidity — will the lights stay on?

Most bankruptcies are cash deaths, not “the brand became unpopular overnight.”

### Current ratio

\[
\text{Current ratio} = \frac{\text{current assets}}{\text{current liabilities}}
\]

Question: if we had to settle short-term bills, would short-term assets cover them?

Suppliers care about this number more than shareholders do. A current ratio below 1 means current bills exceed current assets. That can be fine for a grocer who turns inventory into cash every few days. It is terrifying for a slow manufacturer.

### Quick ratio (acid test)

\[
\text{Quick ratio} = \frac{\text{current assets} - \text{inventory}}{\text{current liabilities}}
\]

Same idea, but inventory is treated as suspect. Fashion leftover may be unsellable. Iron ore is not.

**Who wants which ratio?**

- Luxury fashion: prefer the *quick* ratio. Inventory is the risk.
- A miner with a liquid commodity: current ratio is less misleading.

**The trade-off:** extra liquidity is safety, and safety earns a low return. A pile of cash does not go bankrupt. It also does not build the next factory.

---

## 2. Profitability — is the engine making money?

Always compare profit to a base.

### Profit margin

\[
\text{Profit margin} = \frac{\text{net profit}}{\text{revenue}}
\]

“Per sales dollar, how many cents survive?”

Grocers: tiny margins, huge volume.  
Software and patents: fat margins. Turning sand into chips, or code into licenses, adds more value than moving cereal boxes.

### Return on equity (ROE)

\[
\text{ROE} = \frac{\text{net profit}}{\text{shareholders’ equity}}
\]

“Per dollar the owners left in the business, what did they earn this year?”

This is the celebrity ratio. Managers are judged on it. It is also easy to fake with debt. File 05 (DuPont) is built to stop you from being fooled.

### Return on assets (ROA)

\[
\text{ROA} = \frac{\text{net profit}}{\text{total assets}}
\]

“How much profit did the whole asset pile produce?”  
This ignores how the pile was financed, so it is cleaner operationally than ROE, but still uses net profit (which is after interest).

### EBITDA margin

\[
\text{EBITDA margin} = \frac{\text{EBITDA}}{\text{revenue}}
\]

Useful when depreciation is enormous (utilities, cable networks, heavy plant). Net profit can look modest while cash generation is strong, because the accountant is spreading a long-lived factory across decades.

**A utility fingerprint:** ordinary profit margin, *fat* EBITDA margin. The gap is depreciation.

---

## 3. Leverage — other people’s money

A lever lets you move a rock you should not be able to move. Debt lets owners control assets they could not buy with their own cash.

### House example (learn this cold)

| | All cash | With a mortgage |
|--|----------|-----------------|
| House | 100 | 500 |
| Debt | 0 | 400 |
| Your equity | 100 | 100 |

You are **not richer** in the second house. Equity is still 100. You just control a bigger asset.

If the house rises 10%:

- all cash: you make 10
- mortgaged: house is 550, debt still 400, equity is 150 → you made **50%**

If the house falls 20%:

- all cash: you lose 20%
- mortgaged: house is 400, debt 400, equity **0** → you lost 100%

Leverage multiplies wins *and* losses. That is what is “bad” about it. Nothing else.

Private equity is this mortgage story applied to companies: buy with a little equity and a lot of debt, hope the asset rises.

### Debt to assets

\[
\frac{\text{total debt}}{\text{total assets}}
\]

Share of the pile funded by debt.

### Debt to capitalization

\[
\frac{\text{debt}}{\text{debt} + \text{equity}}
\]

Ignores operating liabilities (payables, accruals) and focuses on the two *financial* claims: debt vs equity.

### Assets to equity (the magnification factor)

\[
\frac{\text{assets}}{\text{equity}}
\]

If this is 4, owners control four dollars of assets per dollar of their own capital. Banks can be 10. A cash-rich software firm can be close to 1.

This factor is the third piece of DuPont.

### Interest coverage

\[
\frac{\text{EBIT}}{\text{interest expense}}
\]

From the *income statement*, not the balance sheet. “Does this year’s operating profit cover the interest bill?”

- Around **1**: walking a tightrope
- Below **1**: operations do not even cover interest — emergency
- Comfortably above **5–10**: lenders sleep

A related hybrid is **debt / EBITDA** (stock of debt vs a year’s cash-ish earnings). Lenders love it.

### Who should borrow a lot?

Stable cash, committed customers, low threat of sudden irrelevance: utilities, some consumer habits, classic LBO targets.

Who should not: a chip firm that bets the company on a new plant every cycle. **Do not pile financial risk on top of business risk.**

---

## 4. Efficiency — squeezing the assets

### Asset turnover

\[
\text{Asset turnover} = \frac{\text{revenue}}{\text{total assets}}
\]

Sales generated per dollar of assets. Grocers are high. Utilities and software-with-huge-cash-piles can look low (the cash sits there, not selling cereal).

### Inventory turnover and days inventory

\[
\text{Inventory turnover} = \frac{\text{cost of goods sold}}{\text{inventory}}
\]

\[
\text{Days inventory} = \frac{365}{\text{inventory turnover}}
\]

How many times a year the shelf is emptied, and how many days a typical item sits.

| Business | Typical feeling |
|----------|-----------------|
| Fast food | inventory measured in days |
| Grocery | a couple of weeks |
| Bookstore | months |
| Pharma with long-dated product | can be slow |

Higher turnover is financially valuable because inventory is risky capital sitting still.

### Receivables collection period

How many days, on average, until customers pay.

\[
\text{Collection period (days)} \approx \frac{\text{receivables}}{\text{sales}} \times 365
\]

(Desai’s table prints this as a days figure. The idea is what matters.)

- Under ~15 days: mostly consumers paying now
- 30–90 days: selling to businesses
- Thousands of days: you are not looking at a shop. You are looking at a bank’s loan book.

Retail vs B2B is often the first cut in the matching game.

---

## Pocket card

| Family | Star ratios | Owner of the question |
|--------|-------------|------------------------|
| Liquidity | Current, quick | Suppliers, nervous CFOs |
| Profitability | Margin, ROE, ROA, EBITDA margin | Owners, and anyone comparing industries |
| Leverage | Debt/assets, assets/equity, EBIT/interest | Lenders, and owners who like (or fear) magnification |
| Efficiency | Asset turnover, inventory turns, collection days | Operators |

No single ratio is “the truth.” Each is a camera angle.

---

## Check yourself

1. Why might a grocer with a current ratio under 1 still be safe?
2. Two firms have the same ROE. One has fat margins and no debt. The other has thin margins and huge debt. Who is more fragile?
3. Why is the quick ratio stricter than the current ratio?
4. A company’s collection period is 8 days. Consumer or business customer?

**Answers:** (1) Inventory turns into cash in days, faster than supplier bills come due. (2) The levered thin-margin firm. (3) It refuses to count inventory as money you can certainly get. (4) Consumer.

Next: [04 Industry fingerprints](04-industry-fingerprints.md)
