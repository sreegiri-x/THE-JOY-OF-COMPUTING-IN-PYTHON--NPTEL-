

# The Joy of Computing using Python
## Unit 10 - Week 7: Assignment 7

### Case Study: Arjun and the Archivist's Rules
Arjun was an apprentice archivist in the City of Timelines, a place where knowledge was preserved under strict rules. Every object stored in the archive followed a data discipline; nothing was random, and nothing was accidental.

One afternoon, the Chief Archivist handed Arjun two enchanted records. "These are not just containers," she said. "They decide how information behaves."

#### Record One: The Chronicle Scroll
The first record was called the Chronicle Scroll. "This scroll preserves history exactly as it is written," said the Archivist. "Once sealed, its contents can never be altered."

The Archivist explained that the Chronicle Scroll works like a **Tuple**.
`Chronicle Scroll = Tuple`

Arjun recorded the sequence of royal events:
```python
chronicle = ("Coronation", "War Declared", "Peace Treaty")
```

He reviewed the entries:
```python
print(chronicle[1])
# Output: War Declared
```

Encouraged, Arjun tried to revise history:
```python
chronicle[1] = "Secret Negotiation"
```
The archive rejected the change immediately.

**What Arjun Observed:**
* Events stayed in the same order
* Each event had a fixed position
* Once recorded, entries could not be changed
* The scroll allowed repeated events if history demanded it

**Inference:**
Tuples preserve order, are immutable, and can store duplicates. They use round brackets `()`.

---

#### Record Two: The Artifact Vault
The second record was called the Artifact Vault. "This vault only cares about what exists, not how it is arranged," said the Archivist. "And it never keeps the same artifact twice."

The vault behaves like a **Set**.
`Artifact Vault = Set`

Arjun logged collected artifacts:
```python
artifacts = {"ring", "amulet", "ring", "scroll"}
```

When he checked the vault, he saw:
```python
print(artifacts)
# Output (order may vary): {'ring', 'amulet', 'scroll'}
```
The duplicate artifact had vanished.

**Managing the Artifact Vault:**
Unlike the Chronicle Scroll, the vault was flexible. Arjun added a new artifact:
```python
artifacts.add("crystal")
```
Later, he removed one:
```python
artifacts.remove("ring")
```
The vault updated instantly.

**What Arjun Observed:**
* Order was unpredictable
* Duplicate artifacts were automatically ignored
* Items could be added or removed freely
* The vault focused only on uniqueness

**Inference:**
Sets are unordered, mutable, and store only unique elements. They use curly brackets `{}`.

---

### Quiz: Week 7 Assignment

**1) Arjun attempted to change an entry inside the Chronicle Scroll using: `chronicle[1] = "Secret Negotiation"`. Why did this action fail?**
- Because tuples do not support indexing
- Because the element did not exist
- Because the Chronicle Scroll preserves order only
- Because the Chronicle Scroll is immutable

**Correct Answer:**
Because the Chronicle Scroll is immutable

**2) When Arjun created the Artifact Vault as: `artifacts = {"ring", "amulet", "ring", "scroll"}`. Why did the final vault contain fewer items than expected?**
- Because sets automatically sort items
- Because duplicate elements are ignored
- Because only strings are allowed
- Because indexing is not supported

**Correct Answer:**
Because duplicate elements are ignored

**3) Which operation was possible on the Artifact Vault but impossible on the Chronicle Scroll?**
- Accessing an element using index
- Preserving insertion order
- Modifying the container after creation
- Allowing duplicate values

**Correct Answer:**
Modifying the container after creation

**4) Arjun noticed that printing the Artifact Vault showed items in an unpredictable order. What caused this behavior?**
- The vault was empty initially
- Python randomly shuffles set elements
- Sets do not maintain insertion order
- Duplicate elements change ordering

**Correct Answer:**
Sets do not maintain insertion order

**5) Which of the following would raise an error if attempted on the Chronicle Scroll?**
- Checking length
- Accessing an element
- Iterating through elements
- Updating an existing element

**Correct Answer:**
Updating an existing element

**6) Why was the Artifact Vault more suitable for tracking collected artifacts?**
- It supports indexing
- It allows duplicates
- It guarantees uniqueness
- It preserves historical order

**Correct Answer:**
It guarantees uniqueness

**7) If Arjun needed to ensure that historical records could never be altered, which structure was most appropriate?**
- List
- Set
- Dictionary
- Tuple

**Correct Answer:**
Tuple

**8) Which statement about indexing is TRUE based on the case study?**
- Both tuples and sets support indexing
- Only sets support indexing
- Only tuples support indexing
- Neither supports indexing

**Correct Answer:**
Only tuples support indexing

**9) Arjun removed an item from the Artifact Vault successfully. Why was this operation safe?**
- Because sets allow modification
- Because tuples allow removal
- Because removal works only on strings
- Because indexing was used

**Correct Answer:**
Because sets allow modification

**10) Which inference correctly matches both records used by Arjun?**
- Chronicle Scroll: unordered, mutable | Artifact Vault: ordered, immutable
- Chronicle Scroll: ordered, immutable | Artifact Vault: unordered, mutable
- Chronicle Scroll: ordered, immutable | Artifact Vault: ordered, duplicate-allowed

**Correct Answer:**
Chronicle Scroll: ordered, immutable | Artifact Vault: unordered, mutable

---

### Case Study: Meera and the Community Learning Center
Meera volunteered at a community learning center. The center faced recurring problems: student registrations came from different sources, course details were fixed once announced, attendance had to be tracked, and records needed to be stored for audits.

#### Step 1: Fixed Course Information (Tuples)
At the start of the month, course details were finalized and never changed afterward.
```python
python_course = (101, "Python Basics", 6)
data_course = (102, "Data Analysis", 8)
web_course = (103, "Web Development", 10)
```

#### Step 2: Managing Student Registrations (Lists)
Student registrations arrived daily, and new names had to be added continuously.
```python
students = ["Aarav", "Neha", "Ishaan"]
students.append("Mehul")
students.append("Neha")
```

#### Step 3: Mapping Students to Courses (Dictionary)
Each student enrolled in one course only.
```python
enrollments = {
    "Aarav": python_course,
    "Neha": data_course,
    "Ishaan": python_course,
    "Mehul": web_course
}
```

#### Step 4: Tracking Attendance per Student (Dictionary + List)
Attendance changed every day, so Meera needed a mutable structure.
```python
attendance = {
    "Aarav": [1, 2, 3],
    "Neha": [1, 2],
    "Ishaan": [1, 3],
    "Mehul": []
}

# Later updates:
attendance["Mehul"].append(1)
attendance["Neha"].append(3)
```

#### Step 5: Saving Records to a File (File Handling)
```python
with open("enrollments.txt", "w") as file:
    for student, course in enrollments.items():
        file.write(f"{student} - {course[1]} ({course[2]} weeks)\n")
```

#### Step 6: Reading Stored Records Later
```python
with open("enrollments.txt", "r") as file:
    records = file.readlines()
for line in records:
    print(line.strip())
```

---

### Quiz Continued

**11) Suppose the following change is made before writing to the file:**
```python
python_course = (101, "Python Basics", 6)
python_course[2] = 7
```
**What would be the first issue encountered in the program?**
- The file will store incorrect duration
- A runtime error will occur due to tuple immutability
- The dictionary enrollments will update automatically
- The list students will change size

**Correct Answer:**
A runtime error will occur due to tuple immutability

**12) Consider this code is added after reading from the file:**
```python
records = file.readlines()
records.append("Rohan - Python Basics (6 weeks)\n")
```
**Which statement is TRUE?**
- A file write error occurs
- The file content changes automatically
- The new record is saved permanently in enrollments.txt
- Only the in-memory list is modified

**Correct Answer:**
Only the in-memory list is modified

**13) Assume this code is executed:**
```python
attendance["Aarav"].append(4)
enrollments["Aarav"] = (101, "Python Basics", 6)
```
**Which statement best explains what happens?**
- Both operations fail
- Both operations succeed
- Attendance succeeds, enrollment fails
- Enrollment succeeds, attendance fails

**Correct Answer:**
Both operations succeed

**14) If Meera replaces this line:**
```python
students = ["Aarav", "Neha", "Ishaan"]
```
**with:**
```python
students = ("Aarav", "Neha", "Ishaan")
students.append("Mehul")
```
**What is the correct outcome?**
- The student is added successfully
- A runtime error occurs due to unsupported operation
- The tuple expands automatically
- The enrollment file updates

**Correct Answer:**
A runtime error occurs due to unsupported operation

**15) Which design choice in the case study most directly protects course data from accidental modification?**
- Using formatted strings while writing files
- Using lists for attendance tracking
- Reading files using readlines()
- Storing course details as tuples inside dictionaries

**Correct Answer:**
Storing course details as tuples inside dictionaries

---
