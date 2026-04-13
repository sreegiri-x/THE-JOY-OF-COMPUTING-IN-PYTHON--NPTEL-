# Week 10 — Sorting and Algorithmic Thinking: Answers

---

### Q1. Answer: **B) Compares adjacent elements and swaps them if they are in the wrong order**

Bubble sort repeatedly walks through the list comparing and swapping adjacent elements, "bubbling" the largest element to the end with each pass.

---

### Q2. Answer: **C) O(n²)**

Bubble sort has O(n²) worst-case complexity because it uses two nested loops — one for each pass and one for comparisons.

---

### Q3. Answer: **B) `[12, 22, 25, 34, 64]`**

`list.sort()` sorts in ascending order by default.

---

### Q4. Answer: **B) `sorted()` returns a new sorted list; `list.sort()` sorts in place and returns `None`**

`sorted(lst)` does not modify the original list. `lst.sort()` modifies the list in place and returns `None`.

---

### Q5. Answer: **C) O(n²)**

Selection sort always performs O(n²) comparisons, regardless of the input, because it must scan the remaining unsorted portion for the minimum on each pass.

---

### Q6. Answer: **C) Divide the list into halves, sort each half, and merge**

Merge sort is a divide-and-conquer algorithm. It recursively splits the list and then merges sorted halves.

---

### Q7. Answer: **C) O(n log n)**

Quicksort has O(n log n) average-case complexity. Its worst case is O(n²) when the pivot is consistently the smallest or largest element.

---

### Q8. Answer: **B) Sorts in descending order**

`reverse=True` parameter makes `sort()` sort in descending order.

---

### Q9. Answer: **B) `["apple", "banana", "cherry"]`**

`sort()` on strings sorts lexicographically (alphabetical order).

---

### Q10. Answer: **C) Insertion sort**

Insertion sort is very efficient for nearly sorted data because it requires few swaps. Its best-case complexity is O(n) for already-sorted input.

---

## Programming Problem 1 — Solution: Bubble Sort

```python
def bubble_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Sorted:", bubble_sort(numbers))
```

---

## Programming Problem 2 — Solution: Selection Sort

```python
def selection_sort(lst):
    n = len(lst)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Sorted:", selection_sort(numbers))
```

---

## Programming Problem 3 — Solution: Sort by Word Length

```python
words = input("Enter words separated by spaces: ").split()
words.sort(key=len)
print("Sorted by length:", words)
```

**Sample Output:**
```
Enter words separated by spaces: banana apple kiwi cherry fig
Sorted by length: ['fig', 'kiwi', 'apple', 'banana', 'cherry']
```
