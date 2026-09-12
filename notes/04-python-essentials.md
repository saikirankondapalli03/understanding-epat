# 04 — Python essentials (lecture was MATLAB)

**Slides:** 6–34 (same ideas; Chan typed them in MATLAB)

← [03 Four causes](03-four-causes.md) · Next: [05 Futures and roll](05-futures-and-roll-returns.md) →

You do **not** need MATLAB. Everything the lecture coded is in `python/` as `.py` files. This note is the vocabulary those files use.

```
pip install numpy pandas scipy
```

---

## Why any array language

One line should operate on a **whole price history**, not a cell in Excel. MATLAB, R, and Python (NumPy/pandas) all do that. Chan picked MATLAB; we use Python.

Python indexes from **0**. MATLAB indexes from **1**. That is the only gotcha.

```python
import numpy as np
import pandas as pd

y = np.array([0.1, 0.2, 0.3, 0.4, 0.5])
y[0]     # first element  (MATLAB: y(1))
y[-1]    # last element   (MATLAB: y(end))
```

## Arrays (slides 9–13)

```python
A = np.full(3, np.nan)   # missing values
A[0] = 0.1
A[1] = 0.2

X = np.array([1, 3, 4])          # 1-D
Y = np.array([6, 8, 9])
Z = np.concatenate([X, Y])       # side by side
W = np.vstack([X, Y])            # stack as rows

U = 0.8 * np.ones(3)
V = np.zeros((4, 2))
mask = np.zeros((3, 3), dtype=bool)

tickers = ["IBM", "MSFT", "GOOG"]  # ordinary Python list
```

`#` starts a comment.

## Arithmetic (slides 14–16)

```python
z = x + y          # pairwise add
z = x * y          # pairwise multiply
z = x / y          # pairwise divide
z = x @ y          # matrix multiply
A.T                # transpose
np.linalg.inv(A)   # inverse
```

In Python, `*` on arrays is **already** element-by-element. Use `@` (or `np.dot`) for linear algebra.

## Slicing (slides 17–25)

```python
y = np.array([0.1, 0.2, 0.3, 0.4, 0.5])
y[[0, 2]]        # 1st and 3rd
y[0:3]           # first three  (stop index is exclusive)
y[2:]            # 3rd to last
y[::-1]          # reverse
y[::-2]          # reverse, skip every other

x = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
xr = x[0, :]     # first row
xc = x[:, 1]     # second column
```

### Exercise — chronological prices (slides 19–20)

Data is newest-first. Make it oldest-first:

```python
data = data[::-1]                 # reverse rows
# or
data = np.flipud(data)
# or, if column 0 is the date:
data = data.sort_values(data.columns[0])
```

### Logical selection (slides 21–22)

```python
x = np.array([1.3, -2, 4, 5])
x[x > 2]                 # array([4, 5])
idx = np.where(v > 5)[0] # positions, not values
v[idx]
```

### Delete (slides 23–25)

```python
x = np.delete(x, [0, 2])          # drop elements
x = np.delete(x, 0, axis=0)       # drop first row
data = data[data[:, 1] >= 0.5]    # keep rows whose 2nd column is >= 0.5
```

## The two functions you must be able to write

### Lag a series (slides 28–30) — MATLAB called this `mybackshift`

Yesterday’s close sits on **today’s** row. The first row is missing (`NaN`).

```python
def lag(series, periods=1):
    return pd.Series(series).shift(periods)

cls = pd.Series([11, 12, 13, 14])
lag(cls, 1)   # [NaN, 11, 12, 13]
```

Daily return:

```python
dailyret = (cls - lag(cls, 1)) / lag(cls, 1)
# same thing:
dailyret = cls.pct_change()
```

Ready-made: `python/helpers.py` → `lag`, `daily_return`.

### Moving average (slides 31–32)

```python
def moving_average(x, lookback):
    return pd.Series(x).rolling(lookback).mean()
```

First `lookback - 1` rows are `NaN` because there is not enough history.

---

## Check yourself

1. What is `x * y` vs `x @ y` on 2-D NumPy arrays?
2. Write the one-liner that reverses all rows of `data`.
3. Why does a lagged close start with `NaN`?

Answers: (1) `*` pairwise, `@` matrix multiply. (2) `data[::-1]`. (3) There is no “yesterday” for the first day.

Next: [05 Futures and roll returns](05-futures-and-roll-returns.md)
