# Writing good functions

The purpose of this lesson today is to write as many functions as we can in the best way we can.

## Guidelines

1. All numbers must be formatted in lacs (00,00,000) and crores (00,00,00,000)
2. Precision to two decimal places is required. Round any additional precision to two decimal places.
3. 

## Worksheet

**1. Simple Interest**

Write a function `simple_interest(principal, term, rate)` that returns the total value of the `principal` that grows simply at the `rate` (per annum) for the given `term` in years.

```python
>>> simple_interest(123456, 23, 0.08)
3,50,615
```

**2. Compound Interest (Basic)**

Write a function `compound_interest(principal, term, rate)` that returns the total value of the `principal` that grows at the compounded `rate` (per annum) for the given `term` in years.

```python
>>> compound_interest(123456, 23, 0.08)
7,24,867
```

**3. Compound Interest (Advanced)**

Write a function `compound_interest_with_payments(principal, payment, term, rate, end_of_period=True)` that returns the total value of the `principal` that grows at the compounded `rate` (per annum) for the given `term` in years assuming that an additional amount of `payment` is added to the amount per term.

`end_of_period` determines whether the additional payment was made at the start or end of the interval and will affect the calcualtion.

Round the result to the nearest paisa.

```python
>>> compound_interest_with_payments(0, 100000, 35, 0.10)
2,36,02,436.85
```

```python
>>> compound_interest_with_payments(0, 368970.52, 35, 0.10)
10,00,00,002.17
```

**4. Savings Calculator**

Write a function `savings_calculator(present_value, future_value, term, rate, end_of_period=True)` which calculates the required payment per interval such that the compounded value given the other parameters will yield a final value equal to `future_value` at the end of `term`.

Round the number up to the nearest paisa.

```python
>>> savings_calculator(0, 1e8, 35, 0.10)
3,68,970.52
```
