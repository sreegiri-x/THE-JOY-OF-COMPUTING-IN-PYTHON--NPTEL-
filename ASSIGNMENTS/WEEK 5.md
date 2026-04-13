
# The Joy of Computing using Python
## Unit 8 - Week 5: Assignment 5

### Dilrez Builds a Smart Student Record System
Dilrez is a teaching assistant who is asked to create a Smart Student Record System for a small institute. The system must store, update, analyze, and report student data efficiently. To achieve this, Dilrez chooses Python Dictionaries because:
* Each student has a unique roll number
* Each roll number maps to multiple details
* Data needs to be updated, searched, and processed quickly

#### 1. What Is a Dictionary? (Key-Value Mapping)
A dictionary stores data in `key: value` form.

```python
student = {
    "roll": 101,
    "name": "Ayaan",
    "age": 20
}
```

#### 2. Accessing Dictionary Data
```python
print(student["name"])
print(student.get("age"))
```
`.get()` is safer because it does not cause an error if the key is missing.

#### 3. Adding & Updating Data in a Dictionary
Dilrez now wants to add marks.
```python
student["marks"] = 85
student["age"] = 21
```

#### 4. Dictionary of Lists (One Student, Multiple Scores)
Each student has marks in multiple tests.
```python
student = {
    "roll": 101,
    "name": "Ayaan",
    "marks": [78, 85, 90]
}
```
**Processing the list inside a dictionary:**
```python
average = sum(student["marks"]) / len(student["marks"])
print(average)
```

#### 5. Dictionary of Dictionaries (Structured Records)
Now Dilrez stores multiple students.
```python
students = {
    101: {"name": "Ayaan", "marks": [78, 85, 90]},
    102: {"name": "Riya", "marks": [88, 92, 79]},
    103: {"name": "Kabir", "marks": [70, 75, 80]}
}
```
**Accessing nested data:**
```python
print(students[102]["name"])
print(students[101]["marks"][1])
```

#### 6. List of Dictionaries (Row-Wise Data)
Sometimes data comes row-by-row (like Excel).
```python
students = [
    {"roll": 101, "name": "Ayaan", "marks": 85},
    {"roll": 102, "name": "Riya", "marks": 90},
    {"roll": 103, "name": "Kabir", "marks": 78}
]
```
**Searching in list of dictionaries:**
```python
for student in students:
    if student["roll"] == 102:
        print(student["name"])
```

#### 7. Looping Through Dictionaries
* **Keys only:** `for key in student: print(key)`
* **Values only:** `for value in student.values(): print(value)`
* **Key-Value pairs:** `for key, value in student.items(): print(key, value)`

---

### Assignment Questions

**1) Dilrez wants to extract the first test score of Riya from a nested student record. What will be printed?**
```python
students = {
    101: {"name": "Ayaan", "marks": [78, 85, 90]},
    102: {"name": "Riya", "marks": [88, 92, 79]}
}
print(students[102]["marks"][0])
```
- 92
- 79
- **88** (Accepted Answer)
- Error

**2) A new test score is added for Kabir. How many marks does Kabir finally have?**
```python
student = {
    "name": "Kabir",
    "marks": [70, 75, 80]
}
student["marks"].append(85)
print(len(student["marks"]))
```
- 3
- 85
- **4** (Accepted Answer)
- Error

**3) Dilrez modifies a list stored inside a dictionary and then reuses the same reference. What is printed?**
```python
data = {"nums": [1, 2, 3]}
ref = data["nums"]
ref.append(4)
print(data["nums"])
```
- [1, 2, 3]
- **[1, 2, 3, 4]** (Accepted Answer)
- Error
- [4]

**4) Dilrez slices a list obtained from a dictionary and modifies the slice. What happens to the original list?**
```python
student = {"marks": [10, 20, 30, 40]}
subset = student["marks"][:2]
subset.append(99)
print(student["marks"])
```
- **[10, 20, 30, 40]** (Accepted Answer)
- [10, 20, 99]
- Error
- [10, 20]

**5) A function reassigns a dictionary parameter instead of mutating it. What value is printed?**
```python
def update(d):
    d = {"x": 100}

data = {"x": 10}
update(data)
print(data["x"])
```
- **10** (Accepted Answer)
- 100
- None
- Error

**6) Dilrez modifies a dictionary while iterating over its keys without creating a copy. What happens when the code runs?**
```python
data = {"a": 1, "b": 2}
for k in data.keys():
    if k == "a":
        data["c"] = 3
print(len(data))
```
- 2
- 3
- 1
- **Runtime Error** (Accepted Answer)

**7) Dilrez draws a bar graph to compare students fairly... Which student's bar will be the tallest?**
*Data: Ayaan: [70, 80, 90], Riya: [85, 90], Kabir: [60, 65, 70, 75]*
- Kabir
- Ayaan
- **Riya** (Accepted Answer)
- All bars will be equal

**8) Dilrez plots a line graph showing performance of each test across all students. Which test appears as the highest point?**
*Data: Student 1: [50, 60, 70], Student 2: [60, 70, 88], Student 3: [70, 80, 90]*
- Test 2
- Test 1
- **Test 3** (Accepted Answer)
- All tests overlap

---

### Case Study: Searching for a Book ID

#### Linear Search
* **Idea:** Checking books one by one starting from the first.
* **Logic:** Works for any list; no sorting required.

```python
def linear_search(a, x):
    count = 0
    for i in range(len(a)):
        count += 1
        if a[i] == x:
            print(f"Element found at position {i}.")
            return count
    print("Number is not present.")
    return count
```

#### Binary Search
* **Idea:** Opening a dictionary at the middle, then deciding left or right.
* **Requirement:** The list **must be sorted**.

```python
def binary_search(a, x):
    first_pos = 0
    last_pos = len(a) - 1
    flag = 0
    count = 0
    while first_pos <= last_pos and flag == 0:
        count += 1
        mid = (first_pos + last_pos) // 2
        if x == a[mid]:
            flag = 1
            print(f"Element found at position {mid}")
            return count
        elif x < a[mid]:
            last_pos = mid - 1
        else:
            first_pos = mid + 1
    print("Number is not present.")
    return count
```

---

**11) A list contains 10 sorted elements. The target element is located at index 6. Using linear search, how many iterations will be counted?**
- 6
- **7** (Accepted Answer)
- 10
- 5

**12) In the binary search implementation, what primarily causes the number of iterations to reduce compared to linear search?**
- **The loop runs fewer times due to index jumps** (Accepted Answer)
- The use of a flag variable
- The list length is fixed
- Elements are compared sequentially

**13) If the searched element is not present in a list of 10 elements...**
- **Linear search will check all elements** (Accepted Answer)
- Binary search will always run exactly 10 times
- Binary search cannot handle missing elements

**14) If elements increase from 10 to 1,000, which graph represents growth for binary search?**
- **A slowly rising curve** (Accepted Answer)
- A flat horizontal line
- A steep straight line

**15) If the list were unsorted but binary search logic was applied:**
- **The element may not be found even if present** (Accepted Answer)
- The algorithm would still work but slower
- Python would raise a runtime error

---
