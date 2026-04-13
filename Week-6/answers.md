# Week 6 — Strings: Answers

---

### Q1. Answer: **A) W**

`s[7]` accesses the character at index 7. `"Hello, World!"` has indices:
`H=0, e=1, l=2, l=3, o=4, ,=5, (space)=6, W=7`. So `s[7] = 'W'`.

---

### Q2. Answer: **B) nohtyP**

`s[::-1]` reverses the string. `"Python"` reversed is `"nohtyP"`.

---

### Q3. Answer: **C) HELLO**

`upper()` converts all characters to uppercase.

---

### Q4. Answer: **B) hello**

`strip()` removes leading and trailing whitespace from the string.

---

### Q5. Answer: **B) `["hello", "world"]`**

`split()` with no argument splits on whitespace and returns a list of words.

---

### Q6. Answer: **C) 3**

`"banana"` contains three `'a'` characters: b**a**n**a**n**a**.

---

### Q7. Answer: **B) 2**

`"Python".find("th")` returns the starting index of the substring `"th"`. `P=0, y=1, t=2, h=3`, so `"th"` starts at index 2.

---

### Q8. Answer: **A) Hello World**

`+` concatenates strings. `"Hello" + " " + "World"` gives `"Hello World"` (printed without quotes).

---

### Q9. Answer: **B) abcabcabc**

`*` repeats a string. `"abc" * 3` gives `"abcabcabc"`.

---

### Q10. Answer: **C) `startswith()`**

Python's string method is `startswith()` (lowercase `w`). Note: `startsWith()` is JavaScript syntax.

---

## Programming Problem 1 — Solution

```python
sentence = input("Enter a sentence: ")
vowels = "aeiouAEIOU"
count = sum(1 for ch in sentence if ch in vowels)
print(f"Number of vowels: {count}")
```

**Sample Output:**
```
Enter a sentence: Hello World
Number of vowels: 3
```

---

## Programming Problem 2 — Solution

```python
s = input("Enter a string: ").lower().replace(" ", "")
if s == s[::-1]:
    print(f'"{s}" is a Palindrome')
else:
    print(f'"{s}" is NOT a Palindrome')
```

**Sample Output:**
```
Enter a string: racecar
"racecar" is a Palindrome
```

---

## Programming Problem 3 — Solution

```python
sentence = input("Enter a sentence: ").lower()
words = sentence.split()
frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("Word frequencies:")
for word, count in frequency.items():
    print(f"  {word}: {count}")
```

**Sample Output:**
```
Enter a sentence: to be or not to be
Word frequencies:
  to: 2
  be: 2
  or: 1
  not: 1
```
