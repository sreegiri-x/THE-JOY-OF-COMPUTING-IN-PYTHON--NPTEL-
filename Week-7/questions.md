# Week 7 — Dictionaries and Sets

## Assignment Questions

---

### Q1. What is the output of the following?

```python
d = {"a": 1, "b": 2, "c": 3}
print(d["b"])
```

- A) `"b"`
- B) `1`
- C) `2`
- D) `3`

---

### Q2. What does the following code print?

```python
d = {"x": 10}
d["y"] = 20
print(len(d))
```

- A) `1`
- B) `2`
- C) `3`
- D) `Error`

---

### Q3. Which method returns all keys of a dictionary?

- A) `d.values()`
- B) `d.items()`
- C) `d.keys()`
- D) `d.all()`

---

### Q4. What is the output of the following?

```python
d = {"a": 1, "b": 2}
print(d.get("c", 0))
```

- A) `None`
- B) `Error`
- C) `0`
- D) `"c"`

---

### Q5. What is the output of the following?

```python
s = {1, 2, 3, 2, 1}
print(len(s))
```

- A) `5`
- B) `3`
- C) `2`
- D) `Error`

---

### Q6. What is the output of the following set operation?

```python
a = {1, 2, 3}
b = {2, 3, 4}
print(a & b)
```

- A) `{1, 2, 3, 4}`
- B) `{2, 3}`
- C) `{1, 4}`
- D) `{1, 2, 3, 2, 3, 4}`

---

### Q7. What does `a | b` represent for two sets `a` and `b`?

- A) Intersection
- B) Difference
- C) Union
- D) Symmetric difference

---

### Q8. What is the output of the following?

```python
d = {"name": "Alice", "age": 25}
for key, value in d.items():
    print(key, "->", value)
```

- A) `name age`
- B) `Alice 25`
- C) `name -> Alice` and `age -> 25`
- D) `Error`

---

### Q9. What happens if you try to access a key that does not exist in a dictionary using `d["key"]`?

- A) Returns `None`
- B) Returns `0`
- C) Raises `KeyError`
- D) Creates the key with value `None`

---

### Q10. Can a set contain duplicate values?

- A) Yes
- B) No — sets automatically remove duplicates
- C) Only if the values are integers
- D) Only with the `allow_duplicates=True` flag

---

### Programming Problem 1

Write a Python program that creates a dictionary of 5 students and their marks, then prints the name of the student with the **highest marks**.

---

### Programming Problem 2

Write a Python program to find the **union**, **intersection**, and **difference** of two sets entered by the user.

---

### Programming Problem 3

Write a Python program that counts how many times each character appears in a given string using a dictionary.
