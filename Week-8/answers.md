# Week 8 — File Handling and Modules: Answers

---

### Q1. Answer: **B) `open()`**

`open(filename, mode)` is the built-in function to open files in Python.

---

### Q2. Answer: **C) `"w"`**

`"w"` opens for writing. If the file exists, it is overwritten. If it doesn't, it is created. `"a"` appends, `"r"` reads, `"x"` creates exclusively (fails if file exists).

---

### Q3. Answer: **B) Hello**

The program first writes `"Hello"` to `test.txt`, then reads and prints it.

---

### Q4. Answer: **C) Opens for appending — writes to the end of the file**

`"a"` mode keeps existing content and adds new content at the end.

---

### Q5. Answer: **B) `from math import sqrt; sqrt(16)`**

When you use `from math import sqrt`, you can call `sqrt()` directly without the `math.` prefix. Option A would fail because `sqrt` isn't in the global scope without importing it properly.

---

### Q6. Answer: **B) 3**

`math.floor()` rounds down to the nearest integer. `floor(3.9) = 3`.

---

### Q7. Answer: **B) A random integer between 1 and 6 (both inclusive)**

`randint(a, b)` returns a random integer `N` such that `a <= N <= b`.

---

### Q8. Answer: **B) `readlines()`**

`readlines()` reads all lines and returns them as a list of strings (each line includes the newline character `\n`).

---

### Q9. Answer: **B) It ensures the file is properly closed even if an error occurs**

The `with` statement is a context manager. It automatically calls `f.close()` when the block exits, even if an exception occurs.

---

### Q10. Answer: **D) All of the above**

- `datetime` — comprehensive date/time handling
- `time` — time-related functions (e.g., `time.sleep()`)
- `calendar` — calendar operations

---

## Programming Problem 1 — Solution

```python
# Write numbers 1-10 to file
with open("numbers.txt", "w") as f:
    for i in range(1, 11):
        f.write(f"{i}\n")

# Read and print the file
print("File contents:")
with open("numbers.txt", "r") as f:
    print(f.read())
```

---

## Programming Problem 2 — Solution

```python
import random

rolls = [random.randint(1, 6) for _ in range(10)]
print("Dice rolls:", rolls)

most_frequent = max(set(rolls), key=rolls.count)
print(f"Most frequent outcome: {most_frequent} (appeared {rolls.count(most_frequent)} times)")
```

---

## Programming Problem 3 — Solution

```python
filename = input("Enter the filename: ")
try:
    with open(filename, "r") as f:
        content = f.read()
    words = content.split()
    print(f"Total words in '{filename}': {len(words)}")
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
```
