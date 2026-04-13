# Week 9 — Recursion and Searching: Answers

---

### Q1. Answer: **B) A function that calls itself**

Recursion is a programming technique where a function solves a problem by calling itself with a simpler version of the same problem.

---

### Q2. Answer: **B) The condition that stops the recursion**

Without a base case, recursion would continue indefinitely. The base case returns a value directly without making further recursive calls.

---

### Q3. Answer: **B) 3 2 1 Go!**

`countdown(3)` prints `3`, calls `countdown(2)` → prints `2`, calls `countdown(1)` → prints `1`, calls `countdown(0)` → prints `"Go!"`.

---

### Q4. Answer: **C) O(n)**

In the worst case, linear search must check every element, making it O(n).

---

### Q5. Answer: **C) O(log n)**

Each step of binary search eliminates half of the remaining elements, giving a logarithmic time complexity.

---

### Q6. Answer: **B) The list must be sorted**

Binary search relies on the sorted order to decide whether to search the left or right half.

---

### Q7. Answer: **B) 16**

`power(2, 4) = 2 * power(2, 3) = 2 * 2 * power(2, 2) = 2 * 2 * 2 * power(2, 1) = 2 * 2 * 2 * 2 * power(2, 0) = 2 * 2 * 2 * 2 * 1 = 16`

---

### Q8. Answer: **B) We compare the target with the middle element and eliminate half the list**

Binary search compares the target with the midpoint, then continues searching in either the left or right half.

---

### Q9. Answer: **B) It runs infinitely and causes a `RecursionError`**

Python has a default recursion limit (~1000 calls). Exceeding it raises a `RecursionError: maximum recursion depth exceeded`.

---

### Q10. Answer: **B) 6**

`sum_digits(123)`:
- `3 + sum_digits(12)` → `3 + 2 + sum_digits(1)` → `3 + 2 + 1 + sum_digits(0)` → `3 + 2 + 1 + 0 = 6`

---

## Programming Problem 1 — Solution

```python
def sum_list(lst):
    if len(lst) == 0:
        return 0
    return lst[0] + sum_list(lst[1:])

print(sum_list([1, 2, 3, 4, 5]))  # 15
```

---

## Programming Problem 2 — Solution

```python
def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1

lst = [4, 2, 7, 1, 9, 3]
target = int(input("Enter target: "))
index = linear_search(lst, target)
if index != -1:
    print(f"Found at index {index}")
else:
    print("Not found")
```

---

## Programming Problem 3 — Solution

```python
def binary_search(lst, target):
    low, high = 0, len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

lst = sorted([4, 2, 7, 1, 9, 3])
print("Sorted list:", lst)
target = int(input("Enter target: "))
index = binary_search(lst, target)
if index != -1:
    print(f"Found at index {index}")
else:
    print("Not found")
```
