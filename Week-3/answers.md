# Week 3 — Loops and Iteration: Answers

---

### Q1. Answer: **B) 0 1 2 3 4**

`range(5)` generates `0, 1, 2, 3, 4`. The `end=" "` replaces the newline with a space.

---

### Q2. Answer: **B) 5**

`i` starts at 1 and increments until it reaches 6 (`> 5`). The loop body runs for `i = 1, 2, 3, 4, 5` → 5 times.

---

### Q3. Answer: **A) 2 5 8**

`range(2, 10, 3)` starts at 2, steps by 3: `2, 5, 8`. The next value would be 11 which exceeds 10.

---

### Q4. Answer: **B) Exits the loop immediately**

`break` terminates the loop and execution continues after the loop body.

---

### Q5. Answer: **B) Skips the rest of the current iteration and moves to the next**

`continue` jumps to the next iteration without executing the remaining statements in the current one.

---

### Q6. Answer: **B) 15**

`1 + 2 + 3 + 4 + 5 = 15`

---

### Q7. Answer: **B) 0 1 2**

When `i == 3`, `break` exits the loop. Before that, `0`, `1`, and `2` are printed.

---

### Q8. Answer: **C) 1 3 5**

`continue` skips even numbers (`2` and `4`), so only `1`, `3`, and `5` are printed.

---

### Q9. Answer: **B) `for i in range(10, 0, -1):`**

`range(10, 0, -1)` generates `10, 9, 8, ..., 1`. A negative step makes the range count down. The stop value `0` is excluded.

---

### Q10. Answer: **A) 1 2 2 4**

- `i=1, j=1`: `1*1=1`
- `i=1, j=2`: `1*2=2`
- `i=2, j=1`: `2*1=2`
- `i=2, j=2`: `2*2=4`

Result: `1 2 2 4`

---

## Programming Problem 1 — Solution

```python
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
```

**Sample Output:**
```
Enter a number: 7
7 x 1 = 7
7 x 2 = 14
...
7 x 10 = 70
```

---

## Programming Problem 2 — Solution

```python
total = 0
for i in range(2, 101, 2):
    total += i
print(f"Sum of even numbers from 1 to 100 = {total}")
```

**Output:** `Sum of even numbers from 1 to 100 = 2550`

---

## Programming Problem 3 — Solution

```python
num = int(input("Enter a number: "))
is_prime = True

if num < 2:
    is_prime = False
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"{num} is a Prime number")
else:
    print(f"{num} is NOT a Prime number")
```

**Sample Output:**
```
Enter a number: 17
17 is a Prime number
```
