# Week 10 — Sorting and Algorithmic Thinking

## Assignment Questions

---

### Q1. What does **bubble sort** do in each pass?

- A) Finds the minimum element and places it at the beginning
- B) Compares adjacent elements and swaps them if they are in the wrong order
- C) Splits the list in half and merges sorted halves
- D) Picks a pivot and partitions the list

---

### Q2. What is the worst-case time complexity of bubble sort?

- A) O(n)
- B) O(n log n)
- C) O(n²)
- D) O(log n)

---

### Q3. What is the output of the following?

```python
lst = [64, 34, 25, 12, 22]
lst.sort()
print(lst)
```

- A) `[64, 34, 25, 12, 22]`
- B) `[12, 22, 25, 34, 64]`
- C) `[64, 34, 25, 22, 12]`
- D) `Error`

---

### Q4. What does `sorted()` return compared to `list.sort()`?

- A) Both modify the list in place
- B) `sorted()` returns a new sorted list; `list.sort()` sorts in place and returns `None`
- C) `sorted()` sorts in place; `list.sort()` returns a new list
- D) There is no difference

---

### Q5. What is the time complexity of selection sort?

- A) O(n)
- B) O(n log n)
- C) O(n²)
- D) O(1)

---

### Q6. What is the main idea behind **merge sort**?

- A) Swap adjacent elements
- B) Find the minimum and place it first
- C) Divide the list into halves, sort each half, and merge
- D) Pick a pivot and partition

---

### Q7. What is the average time complexity of **quicksort**?

- A) O(n²)
- B) O(n)
- C) O(n log n)
- D) O(log n)

---

### Q8. What does `lst.sort(reverse=True)` do?

- A) Sorts in ascending order
- B) Sorts in descending order
- C) Reverses the list without sorting
- D) Raises an error

---

### Q9. What is the output of the following?

```python
words = ["banana", "apple", "cherry"]
words.sort()
print(words)
```

- A) `["banana", "apple", "cherry"]`
- B) `["apple", "banana", "cherry"]`
- C) `["cherry", "banana", "apple"]`
- D) `Error`

---

### Q10. Which sorting algorithm is efficient for nearly sorted data?

- A) Quick sort
- B) Merge sort
- C) Insertion sort
- D) Selection sort

---

### Programming Problem 1

Implement **bubble sort** in Python without using built-in sort functions.

---

### Programming Problem 2

Implement **selection sort** in Python without using built-in sort functions.

---

### Programming Problem 3

Write a Python program that takes a list of words and sorts them by their **length** (shortest first).
