# Week 3 — Loops and Iteration

## Assignment Questions

---

### Q1. What is the output of the following code?

```python
for i in range(5):
    print(i, end=" ")
```

- A) `1 2 3 4 5`
- B) `0 1 2 3 4`
- C) `0 1 2 3 4 5`
- D) `1 2 3 4`

---

### Q2. How many times will the following loop execute?

```python
i = 1
while i <= 5:
    i += 1
```

- A) 4
- B) 5
- C) 6
- D) Infinite

---

### Q3. What is the output of the following code?

```python
for i in range(2, 10, 3):
    print(i, end=" ")
```

- A) `2 5 8`
- B) `2 4 6 8`
- C) `3 6 9`
- D) `2 3 4 5 6 7 8 9`

---

### Q4. What does the `break` statement do in a loop?

- A) Skips the current iteration
- B) Exits the loop immediately
- C) Restarts the loop
- D) Does nothing

---

### Q5. What does the `continue` statement do in a loop?

- A) Exits the loop
- B) Skips the rest of the current iteration and moves to the next
- C) Restarts the entire loop
- D) Pauses the loop

---

### Q6. What is the output of the following?

```python
total = 0
for i in range(1, 6):
    total += i
print(total)
```

- A) `10`
- B) `15`
- C) `14`
- D) `6`

---

### Q7. What is the output of the following code?

```python
i = 0
while i < 5:
    if i == 3:
        break
    print(i, end=" ")
    i += 1
```

- A) `0 1 2 3`
- B) `0 1 2`
- C) `0 1 2 3 4`
- D) `1 2 3`

---

### Q8. What is the output of the following code?

```python
for i in range(1, 6):
    if i % 2 == 0:
        continue
    print(i, end=" ")
```

- A) `2 4`
- B) `1 2 3 4 5`
- C) `1 3 5`
- D) `2 4 6`

---

### Q9. Which of the following loops will print numbers from 10 down to 1?

- A) `for i in range(10, 0):`
- B) `for i in range(10, 0, -1):`
- C) `for i in range(0, 10, -1):`
- D) `for i in range(10):`

---

### Q10. What is the output of the following nested loop?

```python
for i in range(1, 3):
    for j in range(1, 3):
        print(i * j, end=" ")
```

- A) `1 2 2 4`
- B) `1 2 3 4`
- C) `1 4`
- D) `2 4 6`

---

### Programming Problem 1

Write a Python program to print the multiplication table of a number entered by the user (from 1 to 10).

---

### Programming Problem 2

Write a Python program to find the sum of all even numbers between 1 and 100 (inclusive).

---

### Programming Problem 3

Write a Python program to check if a given number is **prime**.
