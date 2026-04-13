# Week 5 — Lists and Tuples: Answers

---

### Q1. Answer: **C) 3**

List indexing starts at `0`. `lst[2]` is the third element, which is `3`.

---

### Q2. Answer: **B) 50**

Negative indexing counts from the end. `lst[-1]` is the last element, `50`.

---

### Q3. Answer: **C) `[1, 2, 3, 4]`**

`append(4)` adds `4` to the end of the list.

---

### Q4. Answer: **B) `[1, 2, 3, 4, 5]`**

`sort()` sorts the list in ascending order in-place.

---

### Q5. Answer: **B) Lists are mutable; tuples are immutable**

Lists (defined with `[]`) can be changed after creation. Tuples (defined with `()`) cannot be modified.

---

### Q6. Answer: **B) 2**

`t[1]` accesses the second element of the tuple, which is `2`.

---

### Q7. Answer: **B) `[1, 2, 3]`**

`lst[1:4]` slices from index 1 (inclusive) to index 4 (exclusive), giving `[1, 2, 3]`.

---

### Q8. Answer: **B) 4**

`len()` returns the number of elements. The list has 4 elements.

---

### Q9. Answer: **B) `[1, 2, 3, 4]`**

`b = a` makes `b` reference the same list object as `a`. Modifying `b` also modifies `a`.

---

### Q10. Answer: **C) `pop()`**

`pop()` with no argument removes and returns the last element. `pop(i)` removes element at index `i`.

---

## Programming Problem 1 — Solution

```python
n = int(input("How many elements? "))
lst = []
for i in range(n):
    lst.append(int(input(f"Enter element {i+1}: ")))

lst_sorted = sorted(set(lst))
if len(lst_sorted) >= 2:
    print(f"Second largest: {lst_sorted[-2]}")
else:
    print("Not enough distinct elements")
```

---

## Programming Problem 2 — Solution

```python
def get_evens(numbers):
    return [x for x in numbers if x % 2 == 0]

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Even numbers:", get_evens(numbers))
```

**Sample Output:**
```
Enter numbers separated by spaces: 1 2 3 4 5 6
Even numbers: [2, 4, 6]
```

---

## Programming Problem 3 — Solution

```python
lst = list(map(int, input("Enter numbers separated by spaces: ").split()))
reversed_lst = lst[::-1]
print("Reversed list:", reversed_lst)
```

**Sample Output:**
```
Enter numbers separated by spaces: 1 2 3 4 5
Reversed list: [5, 4, 3, 2, 1]
```
