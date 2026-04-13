# Week 9 — Recursion and Searching

## Assignment Questions

---

### Q1. What is recursion?

- A) A loop that repeats a fixed number of times
- B) A function that calls itself
- C) A method of sorting data
- D) A type of data structure

---

### Q2. What is the base case in a recursive function?

- A) The last line of the function
- B) The condition that stops the recursion
- C) The first call to the function
- D) The return value of the function

---

### Q3. What is the output of the following?

```python
def countdown(n):
    if n == 0:
        print("Go!")
    else:
        print(n)
        countdown(n - 1)

countdown(3)
```

- A) `Go! 3 2 1`
- B) `3 2 1 Go!`
- C) `1 2 3 Go!`
- D) `Error`

---

### Q4. What is the time complexity of linear search in the worst case?

- A) O(1)
- B) O(log n)
- C) O(n)
- D) O(n²)

---

### Q5. What is the time complexity of binary search?

- A) O(n)
- B) O(n log n)
- C) O(log n)
- D) O(1)

---

### Q6. What is a prerequisite for binary search?

- A) The list must contain only integers
- B) The list must be sorted
- C) The list must have an even number of elements
- D) The list must not have duplicates

---

### Q7. What will the following code output?

```python
def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

print(power(2, 4))
```

- A) `8`
- B) `16`
- C) `4`
- D) `Error`

---

### Q8. In binary search, what happens at each step?

- A) We scan each element one by one
- B) We compare the target with the middle element and eliminate half the list
- C) We sort the list
- D) We reverse the list

---

### Q9. What happens if a recursive function has no base case?

- A) It returns `None`
- B) It runs infinitely and causes a `RecursionError`
- C) It stops after 100 iterations
- D) It returns `0`

---

### Q10. What is the output of the following code?

```python
def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)

print(sum_digits(123))
```

- A) `123`
- B) `6`
- C) `3`
- D) `12`

---

### Programming Problem 1

Write a recursive Python function `sum_list(lst)` that returns the sum of all elements in a list.

---

### Programming Problem 2

Implement **linear search**: write a function that returns the index of a target value in a list, or `-1` if not found.

---

### Programming Problem 3

Implement **binary search**: write a function that returns the index of a target value in a sorted list, or `-1` if not found.
