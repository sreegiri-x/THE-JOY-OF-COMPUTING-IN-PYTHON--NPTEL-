# Week 1 — Introduction to Python: Answers

---

### Q1. Answer: **B) Hello, World!**

`print()` outputs the string exactly as written inside the quotes (without the quotes themselves).

---

### Q2. Answer: **C) # This is a comment**

In Python, single-line comments start with `#`. Python does not use `//` or `/* */` (those are for C/C++/Java).

---

### Q3. Answer: **C) 8**

`x + y` evaluates to `5 + 3 = 8`.

---

### Q4. Answer: **C) char**

Python does not have a `char` type. Single characters are simply strings of length 1 (`str`).

---

### Q5. Answer: **C) `<class 'float'>`**

`type()` returns the class of the object. `3.14` is a `float`, so the output is `<class 'float'>`.

---

### Q6. Answer: **C) A string**

`input()` always returns a `str`, regardless of what the user types. You must explicitly convert it (e.g., `int(input())`) if you need another type.

---

### Q7. Answer: **B) 8**

`**` is the exponentiation operator. `2 ** 3 = 2³ = 8`.

---

### Q8. Answer: **D) `print()`**

`print()` is the standard function for console output in Python.

---

### Q9. Answer: **B) 42**

`int("42")` converts the string `"42"` to the integer `42`.

---

### Q10. Answer: **C) `num = 10`**

Python uses `=` for assignment. The variable name goes on the left-hand side.

---

## Programming Problem 1 — Solution

```python
name = input("Enter your name: ")
age = input("Enter your age: ")
print(f"Hello, {name}! You are {age} years old.")
```

**Sample Output:**
```
Enter your name: Alice
Enter your age: 20
Hello, Alice! You are 20 years old.
```

---

## Programming Problem 2 — Solution

```python
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
print(f"Area of the rectangle = {area}")
```

**Sample Output:**
```
Enter the length of the rectangle: 5
Enter the width of the rectangle: 3
Area of the rectangle = 15.0
```
