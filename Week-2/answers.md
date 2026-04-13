# Week 2 — Variables, Expressions & Conditionals: Answers

---

### Q1. Answer: **B) 1**

`%` is the modulo (remainder) operator. `10 % 3 = 1` because `10 = 3×3 + 1`.

---

### Q2. Answer: **B) 2**

`//` is integer (floor) division. `5 // 2 = 2` (the decimal part is dropped).

---

### Q3. Answer: **A) Big**

`7 > 5` is `True`, so the `if` block runs and prints `"Big"`.

---

### Q4. Answer: **B) False**

In Python, `0` is falsy. `bool(0)` returns `False`. Any non-zero number is `True`.

---

### Q5. Answer: **B) `==`**

`=` is assignment; `==` is comparison (equality check). Python does not have `===`.

---

### Q6. Answer: **B) Divisible by 3**

`15 % 2 = 1` (not 0, so not Even). `15 % 3 = 0` (divisible by 3), so `"Divisible by 3"` is printed. Once an `elif` branch runs, the rest are skipped.

---

### Q7. Answer: **C) 30**

Step 1: `x = 10 + 5 = 15`  
Step 2: `x = 15 * 2 = 30`

---

### Q8. Answer: **B) False**

`not True` is the logical negation, which is `False`.

---

### Q9. Answer: **A) True**

`a > 2` → `3 > 2` → `True`  
`b < 10` → `5 < 10` → `True`  
`True and True` → `True`

---

### Q10. Answer: **B) `1 <= x <= 10`**

Python supports chained comparisons. `1 <= x <= 10` correctly checks `x >= 1` AND `x <= 10`. Option A excludes the endpoints. Option C uses invalid `=<`. Option D is not valid Python syntax.

---

## Programming Problem 1 — Solution

```python
num = float(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
```

**Sample Output:**
```
Enter a number: -7
Negative
```

---

## Programming Problem 2 — Solution

```python
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    print(f"Largest number is {a}")
elif b >= a and b >= c:
    print(f"Largest number is {b}")
else:
    print(f"Largest number is {c}")
```

**Sample Output:**
```
Enter first number: 12
Enter second number: 45
Enter third number: 30
Largest number is 45.0
```
