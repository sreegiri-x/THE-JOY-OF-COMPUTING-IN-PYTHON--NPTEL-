# Week 7 — Dictionaries and Sets: Answers

---

### Q1. Answer: **C) 2**

`d["b"]` accesses the value associated with key `"b"`, which is `2`.

---

### Q2. Answer: **B) 2**

After `d["y"] = 20`, the dictionary has two keys: `"x"` and `"y"`. `len(d) = 2`.

---

### Q3. Answer: **C) `d.keys()`**

`keys()` returns all keys. `values()` returns all values. `items()` returns key-value pairs.

---

### Q4. Answer: **C) 0**

`d.get("c", 0)` returns the value for key `"c"` if it exists, otherwise returns the default `0`. Since `"c"` is not in `d`, it returns `0`.

---

### Q5. Answer: **B) 3**

Sets do not allow duplicate values. `{1, 2, 3, 2, 1}` stores only the unique values `{1, 2, 3}`, so `len` is `3`.

---

### Q6. Answer: **B) `{2, 3}`**

`&` is the intersection operator for sets. Elements common to both `a` and `b` are `2` and `3`.

---

### Q7. Answer: **C) Union**

`|` gives the union (all elements from both sets, without duplicates). `&` is intersection, `-` is difference, `^` is symmetric difference.

---

### Q8. Answer: **C) `name -> Alice` and `age -> 25`**

`d.items()` returns key-value pairs. The loop prints each pair formatted as `key -> value`.

---

### Q9. Answer: **C) Raises `KeyError`**

Using `d["key"]` for a non-existent key raises a `KeyError`. Use `d.get("key")` to safely return `None` (or a default) instead.

---

### Q10. Answer: **B) No — sets automatically remove duplicates**

Sets are unordered collections of **unique** elements.

---

## Programming Problem 1 — Solution

```python
students = {
    "Alice": 88,
    "Bob": 72,
    "Charlie": 95,
    "Diana": 80,
    "Eve": 91
}

top_student = max(students, key=students.get)
print(f"Student with highest marks: {top_student} ({students[top_student]})")
```

**Output:** `Student with highest marks: Charlie (95)`

---

## Programming Problem 2 — Solution

```python
a = set(map(int, input("Enter elements of set A separated by spaces: ").split()))
b = set(map(int, input("Enter elements of set B separated by spaces: ").split()))

print(f"Union: {a | b}")
print(f"Intersection: {a & b}")
print(f"Difference (A - B): {a - b}")
```

**Sample Output:**
```
Enter elements of set A: 1 2 3 4
Enter elements of set B: 3 4 5 6
Union: {1, 2, 3, 4, 5, 6}
Intersection: {3, 4}
Difference (A - B): {1, 2}
```

---

## Programming Problem 3 — Solution

```python
s = input("Enter a string: ")
char_count = {}
for ch in s:
    char_count[ch] = char_count.get(ch, 0) + 1

print("Character frequencies:")
for ch, count in char_count.items():
    print(f"  '{ch}': {count}")
```

**Sample Output:**
```
Enter a string: hello
Character frequencies:
  'h': 1
  'e': 1
  'l': 2
  'o': 1
```
