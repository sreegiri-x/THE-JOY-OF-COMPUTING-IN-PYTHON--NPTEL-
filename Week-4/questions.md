# Week 4 — Functions

## Assignment Questions

---

### Q1. What is the output of the following code?

```python
def greet():
    print("Hello!")

greet()
```

- A) Nothing is printed
- B) `Hello!`
- C) `greet()`
- D) `Error`

---

### Q2. What is the output of the following?

```python
def add(a, b):
    return a + b

result = add(3, 4)
print(result)
```

- A) `3`
- B) `4`
- C) `7`
- D) `None`

---

### Q3. What will be printed?

```python
def square(x):
    return x * x

print(square(5))
```

- A) `x * x`
- B) `5`
- C) `25`
- D) `10`

---

### Q4. What is a default argument in Python?

- A) An argument that must always be provided
- B) An argument with a preset value if not provided by the caller
- C) An argument that returns a default value
- D) The first argument in any function

---

### Q5. What is the output of the following?

```python
def greet(name="World"):
    print(f"Hello, {name}!")

greet()
greet("Alice")
```

- A) `Hello, World!` only
- B) `Hello, Alice!` only
- C) `Hello, World!` then `Hello, Alice!`
- D) `Error`

---

### Q6. What does a function return if it has no `return` statement?

- A) `0`
- B) `False`
- C) `None`
- D) `Error`

---

### Q7. What is the output of the following?

```python
def modify(lst):
    lst.append(4)

my_list = [1, 2, 3]
modify(my_list)
print(my_list)
```

- A) `[1, 2, 3]`
- B) `[1, 2, 3, 4]`
- C) `[4]`
- D) `Error`

---

### Q8. Which keyword is used to define a function in Python?

- A) `function`
- B) `define`
- C) `def`
- D) `func`

---

### Q9. What is the output of the following?

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(4))
```

- A) `4`
- B) `24`
- C) `12`
- D) `Error`

---

### Q10. What is a `lambda` function in Python?

- A) A function defined using `def` with a single line
- B) An anonymous function defined using the `lambda` keyword
- C) A function that never returns a value
- D) A built-in Python function

---

### Programming Problem 1

Write a function `is_even(n)` that returns `True` if `n` is even and `False` otherwise.

---

### Programming Problem 2

Write a function `fibonacci(n)` that returns the nth Fibonacci number (starting from `fibonacci(0) = 0`, `fibonacci(1) = 1`).

---

### Programming Problem 3

Write a function `celsius_to_fahrenheit(c)` that converts a Celsius temperature to Fahrenheit using the formula `F = (C × 9/5) + 32`.
