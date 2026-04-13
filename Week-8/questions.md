# Week 8 — File Handling and Modules

## Assignment Questions

---

### Q1. Which function is used to open a file in Python?

- A) `file()`
- B) `open()`
- C) `read()`
- D) `load()`

---

### Q2. What mode is used to open a file for writing (creating it if it does not exist, overwriting if it does)?

- A) `"r"`
- B) `"a"`
- C) `"w"`
- D) `"x"`

---

### Q3. What is the output of the following?

```python
with open("test.txt", "w") as f:
    f.write("Hello")

with open("test.txt", "r") as f:
    print(f.read())
```

- A) `Error`
- B) `Hello`
- C) Nothing
- D) `test.txt`

---

### Q4. What does `"a"` mode do when opening a file?

- A) Opens for reading
- B) Opens for writing, overwrites existing content
- C) Opens for appending — writes to the end of the file
- D) Opens in binary mode

---

### Q5. Which of the following correctly imports the `math` module and uses `sqrt`?

- A) `import math; sqrt(16)`
- B) `from math import sqrt; sqrt(16)`
- C) `include math; math.sqrt(16)`
- D) `require math; math.sqrt(16)`

---

### Q6. What does `math.floor(3.9)` return?

- A) `4`
- B) `3`
- C) `3.9`
- D) `3.0`

---

### Q7. What does `random.randint(1, 6)` return?

- A) A random float between 1 and 6
- B) A random integer between 1 and 6 (both inclusive)
- C) A random integer between 1 and 5
- D) Always `3`

---

### Q8. Which method reads all lines of a file as a list of strings?

- A) `readall()`
- B) `readlines()`
- C) `readlist()`
- D) `lines()`

---

### Q9. What is the purpose of `with open(...) as f:`?

- A) It opens the file in write mode
- B) It ensures the file is properly closed even if an error occurs
- C) It opens the file for binary reading
- D) It creates a new file

---

### Q10. Which module would you use to work with dates and times?

- A) `time`
- B) `calendar`
- C) `datetime`
- D) All of the above

---

### Programming Problem 1

Write a Python program that writes the numbers 1 to 10 (one per line) to a file called `numbers.txt`, then reads and prints the file contents.

---

### Programming Problem 2

Write a Python program that uses the `random` module to simulate rolling a dice 10 times and prints each result. Also print the most frequent outcome.

---

### Programming Problem 3

Write a Python program that reads a text file provided by the user (filename entered as input) and counts the total number of words in it.
