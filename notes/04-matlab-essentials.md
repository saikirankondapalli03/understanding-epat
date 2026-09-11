# 04 — MATLAB essentials

**Slides:** 6–34

← [03 Four causes](03-four-causes.md) · Next: [05 Futures and roll](05-futures-and-roll-returns.md) →

If the exam is conceptual, skim this file in 20 minutes. You need **lag, returns, logical selection**, not GUIs.

---

## Why MATLAB is in this lecture

It is an **array** language: one line can operate on a whole price history. That makes a backtest short. R and Python can do the same job. Chan’s reasons for MATLAB (toolboxes, support, speed, compile-to-C) are vendor opinions, not finance.

Latency he quotes: MATLAB/R/Python to a broker ~**60 ms** vs C++ **< 1 ms**. MATLAB can be compiled toward C if needed.

## Arrays (slides 9–13)

```matlab
A = NaN(1, 3);   % 1x3, missing values
A(1) = 0.1;
A(2) = 0.2;
A;               % trailing ; stops printing

X = [1 3 4];     % row
Y = [6 8 9];
Z = [X Y];       % concatenate side by side
W = [X; Y];      % stack as rows

U = 0.8 * ones(1, 3);
V = zeros(4, 2);
X = false(3);    % 3x3 logical

Y = {'IBM', 'MSFT', 'GOOG'};  % cell array of tickers
```

- Space or comma: same row.
- Semicolon: new row.
- `%` starts a comment.
- Cell arrays `{...}` hold strings (orders, news).

## Arithmetic (slides 14–16)

Old way: a `for` loop. MATLAB way: vectorized.

```matlab
z = x + y;     % pairwise add
z = x .* y;    % pairwise multiply  (the DOT matters)
z = x ./ y;    % pairwise divide
x * y;         % matrix multiply (no dot)
A';            % transpose
inv(A);        % inverse
```

**Dot = element by element. No dot = linear algebra.**

## Slicing (slides 17–25)

```matlab
y = [0.1 0.2 0.3 0.4 0.5];
y([1 3]);          % 1st and 3rd
y([1:3 5]);        % 1..3 and 5th
y(3:end);          % 3rd to last
y(end:-1:1);       % reverse
y(end:-2:1);       % reverse, skip every other

x = [1 2 3; 4 5 6; 7 8 9];
xr = x(1, :);      % first row
xc = x(:, 2);      % second column
```

### Exercise — chronological prices (slides 19–20)

Data is newest-first. Make it oldest-first:

```matlab
data = data(end:-1:1, :);
% or
data = flipud(data);
% or
data = sortrows(data, 1);
```

### Logical selection (slides 21–22)

```matlab
x = [1.3 -2 4 5];
x(x > 2);          % [4 5]
idx = find(v > 5); % positions, not values
v(idx);
```

### Delete (slides 23–25)

```matlab
x([1 3]) = [];           % drop elements
x(1, :) = [];            % drop first row
data(data(:, 2) < 0.5, :) = [];  % drop rows with col2 < 0.5
```

## Built-in functions (slides 26–27)

Anything that works on a number usually works on an array: `sum`, `cumsum`, `mean`, `std`, `max`, `min`, `corrcoef`, `sortrows`, `isnan`, `plot`, …

Useful toolboxes he names: Datafeed, Trading, Statistics, Financial, Econometrics (GARCH), Optimization, Neural Networks.

## The two functions you must be able to write

### `mybackshift` — lag a series (slides 28–30)

Yesterday’s close is today’s **lagged** close. First `lag` rows become `NaN`; the last `lag` rows fall off.

```matlab
function y = mybackshift(lag, x)
    y = [NaN(lag, size(x, 2)); x(1:end-lag, :)];
end
```

Example: `cls = [11 12 13 14]'` → `mybackshift(1, cls)` is `[NaN 11 12 13]'`.

Daily return:

```matlab
dailyret = (cls - mybackshift(1, cls)) ./ mybackshift(1, cls);
```

### Moving average (slides 31–32)

Sum lags `0 … lookback-1`, divide by lookback. Early rows do not have enough history.

```matlab
function mvavg = movingAvg(x, lookback)
    mvavg = zeros(size(x));
    for i = 0:lookback-1
        mvavg = mvavg + backshift(i, x);
    end
    mvavg = mvavg / lookback;
end
```

(His answer calls `backshift`, not `mybackshift` — same idea.)

## What he skipped (slide 34)

String regex (web scraping), plotting/animation, GUIs. Extra reading: Moler’s MATLAB notes, a UCSD tip sheet, the MATLAB Wikibook.

---

## Check yourself

1. What does `x .* y` do that `x * y` does not?
2. Write the one-liner that reverses all rows of `data`.
3. Why does a lagged close start with `NaN`?

Next: [05 Futures and roll returns](05-futures-and-roll-returns.md)
