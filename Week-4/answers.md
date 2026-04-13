# Week 4 — Functions: Answers

---

### Q1. Answer: **B) Hello!**

Calling `greet()` executes the function body, which prints `"Hello!"`.

---

### Q2. Answer: **C) 7**

`add(3, 4)` returns `3 + 4 = 7`. This is stored in `result` and printed.

---

### Q3. Answer: **C) 25**

`square(5)` returns `5 * 5 = 25`.

---

### Q4. Answer: **B) An argument with a preset value if not provided by the caller**

Default arguments are specified in the function definition: `def greet(name="World")`.

---

### Q5. Answer: **C) `Hello, World!` then `Hello, Alice!`**

First call uses the default `name="World"`. Second call uses `"Alice"`.

---

### Q6. Answer: **C) None**

If a function has no `return` statement (or just `return` with no value), it implicitly returns `None`.

---

### Q7. Answer: **B) `[1, 2, 3, 4]`**

Lists are passed by reference in Python. The function modifies the original list by appending `4`.

---

### Q8. Answer: **C) `def`**

Functions in Python are defined with the `def` keyword.

---

### Q9. Answer: **B) 24**

`factorial(4) = 4 * factorial(3) = 4 * 3 * factorial(2) = 4 * 3 * 2 * factorial(1) = 4 * 3 * 2 * 1 * factorial(0) = 4 * 3 * 2 * 1 * 1 = 24`

---

### Q10. Answer: **B) An anonymous function defined using the `lambda` keyword**

Example: `square = lambda x: x * x`. Lambda functions are short, anonymous, and can only contain a single expression.

---

## Programming Problem 1 — Solution

```python
def is_even(n):
    return n % 2 == 0

# Test
print(is_even(4))   # True
print(is_even(7))   # False
```

---

## Programming Problem 2 — Solution

```python
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Test
for i in range(8):
    print(fibonacci(i), end=" ")
# Output: 0 1 1 2 3 5 8 13
```

---

## Programming Problem 3 — Solution

```python
def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

# Test
temp_c = float(input("Enter temperature in Celsius: "))
print(f"{temp_c}°C = {celsius_to_fahrenheit(temp_c)}°F")
```

**Sample Output:**
```
Enter temperature in Celsius: 100
100.0°C = 212.0°F
```
