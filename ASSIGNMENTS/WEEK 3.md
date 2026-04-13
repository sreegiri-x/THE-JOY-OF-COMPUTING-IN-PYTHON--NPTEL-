

# The Joy of Computing using Python

## Unit 6 - Week 3: Assignment 3

### Case Study: Order Processing System

Riya is building an Order Processing System for an online grocery store. She uses a Python list because it maintains order and allows items to be added, removed, or updated dynamically.

#### 1\. Creating the Order List (Initialization)

At the start of the day, the system has some confirmed orders.

```python
orders = ["Milk", "Bread", "Eggs"]
print(orders)
```

**How this works:**

  * Creates a list
  * Items are stored in order
  * Indexing starts from 0

**Output:** `['Milk', 'Bread', 'Eggs']`

#### 2\. Adding a New Order at the End (append)

A customer orders Butter, which must be added last.

```python
orders.append("Butter")
print(orders)
```

**How this works:**

  * `append()` adds one item at the end
  * Existing order remains unchanged

**Output:** `['Milk', 'Bread', 'Eggs', 'Butter']`

#### 3\. Adding a Priority Order at a Specific Position (insert)

A priority customer orders Fruits, which must come early.

```python
orders.insert(1, "Fruits")
print(orders)
```

**How this works:**

  * `insert(index, value)` places the value at that index
  * Elements from that position shift right

**Output:** `['Milk', 'Fruits', 'Bread', 'Eggs', 'Butter']`

#### 4\. Adding Multiple Orders Together (extend)

A partner store sends additional orders.

```python
partner_orders = ["Rice", "Oil"]
orders.extend(partner_orders)
print(orders)
```

**How this works:**

  * `extend()` adds elements one by one
  * No nested list is created

**Output:** `['Milk', 'Fruits', 'Bread', 'Eggs', 'Butter', 'Rice', 'Oil']`

#### 5\. Accessing a Specific Order (Indexing)

The system checks the first order received.

```python
print(orders[0])
```

**How this works:**

  * Index 0 always refers to the first element

**Output:** `Milk`

#### 6\. Processing Orders in Batches (Slicing)

The packaging team processes the first three orders together.

```python
batch_orders = orders[0:3]
print(batch_orders)
```

**How this works:**

  * Start index included
  * End index excluded
  * Creates a new list

**Output:** `['Milk', 'Fruits', 'Bread']`

#### 7\. Updating an Incorrect Order (Assignment)

A customer ordered Milk but wanted Almond Milk.

```python
orders[orders.index("Milk")] = "Almond Milk"
print(orders)
```

**How this works:**

  * `index()` finds the position of "Milk"
  * Assignment replaces the value at that index

**Output:** `['Almond Milk', 'Fruits', 'Bread', 'Eggs', 'Butter', 'Rice', 'Oil']`

#### 8\. Removing a Cancelled Order by Name (remove)

The Bread order is cancelled.

```python
orders.remove("Bread")
print(orders)
```

**How this works:**

  * `remove()` deletes the first matching element
  * Remaining items shift left

**Output:** `['Almond Milk', 'Fruits', 'Eggs', 'Butter', 'Rice', 'Oil']`

#### 9\. Sorting Orders Alphabetically (sort)

For warehouse efficiency, orders are sorted.

```python
orders.sort()
print(orders)
```

**How this works:**

  * `sort()` rearranges items alphabetically
  * Sorting happens in-place

**Output:** `['Almond Milk', 'Butter', 'Eggs', 'Fruits', 'Oil', 'Rice']`

#### 10\. Clearing All Orders at End of Day (clear)

After delivery, the system resets for the next day.

```python
orders.clear()
print(orders)
```

**How this works:**

  * Removes all elements
  * List still exists but becomes empty

-----

### Quiz: Week 3: Assignment 3

| Q.No | Question and Code Snippet | Options | Correct Answer |
| :--- | :--- | :--- | :--- |
| 1 | `orders = ["Milk", "Bread", "Eggs"]`<br>`orders.append("Butter")`<br>`print(orders)`<br><br>What will be displayed after execution? | A) ['Milk', 'Bread', 'Eggs']<br>B) ['Butter', 'Milk', 'Bread', 'Eggs']<br>C) Error<br>D) ['Milk', 'Bread', 'Eggs', 'Butter'] | **['Milk', 'Bread', 'Eggs', 'Butter']** |
| 2 | `orders = ["Milk", "Bread", "Eggs"]`<br>`orders.insert(1, "Fruits")`<br>`print(orders)`<br><br>Which sequence is produced? | A) ['Milk', 'Bread', 'Eggs', 'Fruits']<br>B) Error<br>C) ['Milk', 'Fruits', 'Bread', 'Eggs']<br>D) ['Fruits', 'Milk', 'Bread', 'Eggs'] | **['Milk', 'Fruits', 'Bread', 'Eggs']** |
| 3 | `orders = ["Milk", "Bread", "Eggs"]`<br>`orders.extend(["Rice", "Oil"])`<br>`print(orders)`<br><br>Which list is printed? | A) ['Milk', 'Bread', 'Eggs', ['Rice', 'Oil']]<br>B) Error<br>C) ['Rice', 'Oil', 'Milk', 'Bread', 'Eggs']<br>D) ['Milk', 'Bread', 'Eggs', 'Rice', 'Oil'] | **['Milk', 'Bread', 'Eggs', 'Rice', 'Oil']** |
| 4 | `orders = ["Milk", "Fruits", "Bread"]`<br>`print(orders[0])`<br><br>Which value appears on the screen? | A) Error<br>B) Bread<br>C) Milk<br>D) Fruits | **Milk** |
| 5 | `orders = ["Milk", "Fruits", "Bread", "Eggs"]`<br>`print(orders[1:3])`<br><br>Which option correctly represents the printed list? | A) ['Milk', 'Fruits']<br>B) ['Bread', 'Eggs']<br>C) ['Fruits', 'Bread', 'Eggs']<br>D) ['Fruits', 'Bread'] | **['Fruits', 'Bread']** |
| 6 | `orders = ["Milk", "Bread", "Eggs"]`<br>`orders.append("Butter")`<br>`orders.sort()`<br>`print(orders)`<br><br>After execution, which arrangement is obtained? | A) ['Butter', 'Bread', 'Eggs', 'Milk']<br>B) ['Bread', 'Butter', 'Eggs', 'Milk']<br>C) Error<br>D) ['Milk', 'Bread', 'Eggs', 'Butter'] | **['Bread', 'Butter', 'Eggs', 'Milk']** |
| 7 | `orders = ["Milk", "Bread", "Eggs"]`<br>`orders.insert(1, "Fruits")`<br>`orders.remove("Bread")`<br>`print(orders)`<br><br>What does the list finally contain? | A) ['Milk', 'Eggs']<br>B) Error<br>C) ['Fruits', 'Milk', 'Eggs']<br>D) ['Milk', 'Fruits', 'Eggs'] | **['Milk', 'Fruits', 'Eggs']** |
| 8 | `orders = ["Milk", "Bread"]`<br>`orders.extend(["Eggs", "Butter", "Rice"])`<br>`print(orders[1:4])`<br><br>Which elements are shown? | A) ['Bread', 'Eggs', 'Butter']<br>B) ['Eggs', 'Butter', 'Rice']<br>C) Error<br>D) ['Milk', 'Bread', 'Eggs'] | **['Bread', 'Eggs', 'Butter']** |
| 9 | `orders = ["Milk", "Bread", "Eggs"]`<br>`orders[orders.index("Milk")] = "Almond Milk"`<br>`orders.sort()`<br>`print(orders)`<br><br>Which list is displayed? | A) ['Bread', 'Eggs', 'Almond Milk']<br>B) Error<br>C) ['Almond Milk', 'Bread', 'Eggs']<br>D) ['Milk', 'Bread', 'Eggs'] | **['Almond Milk', 'Bread', 'Eggs']** |
| 10 | `orders = ["Milk", "Bread", "Eggs"]`<br>`orders.insert(0, "Rice")`<br>`orders.sort()`<br>`print(orders[1:3])`<br><br>Which option correctly matches the program behavior? | A) ['Bread', 'Eggs']<br>B) ['Milk', 'Rice']<br>C) Error<br>D) ['Eggs', 'Milk'] | **['Eggs', 'Milk']** |

-----

### Case Study: Student Performance Analyzer

Ravi is a Teaching Assistant who is preparing a small Python utility to analyze student scores collected from a programming lab. The data comes in raw lists, but the final processed results must be immutable, so Ravi uses tuples.

#### Step 1: Raw Student Marks (List)

```python
marks = [35, 78, 92, 45, 60, 88, 49, 100]
```

This list is mutable, meaning values can change.

#### Step 2: Filtering Passed Students (List Comprehension)

Only students scoring 50 or more are considered passed.

```python
passed = [m for m in marks if m >= 50]
```

  * The expression `m for m in marks` generates values
  * The condition `if m >= 50` filters values
  * The result is a new list, not modifying the original

**Result:** `passed = [78, 92, 60, 88, 100]`

#### Step 3: Adding Bonus Marks (List Comprehension)

Each passed student gets 5 bonus marks, but the total should not exceed 100.

```python
bonus_marks = [min(m + 5, 100) for m in passed]
```

  * `min(m + 5, 100)` ensures marks do not exceed 100
  * This still produces a list

**Result:** `bonus_marks = [83, 97, 65, 93, 100]`

#### Step 4: Converting List to Tuple

Ravi wants to freeze the final results so they cannot be changed accidentally.

```python
final_scores = tuple(bonus_marks)
```

**Result:** `final_scores = (83, 97, 65, 93, 100)`

#### Step 5: Creating Score-Index Pairs

Ravi now wants to tag each score with its index position.

```python
indexed_scores = [(i, final_scores[i]) for i in range(len(final_scores))]
```

**Result:** `indexed_scores = [(0, 83), (1, 97), (2, 65), (3, 93), (4, 100)]`
Each element is a tuple inside a list.

-----

### Quiz Continued (Performance Analyzer)

| Q.No | Question | Options | Correct Answer |
| :--- | :--- | :--- | :--- |
| 11 | What is the value of `passed`? <br> `marks = [35, 78, 92, 45, 60, 88, 49, 100]` <br> `passed = [m for m in marks if m >= 50]` | A) [35, 78, 92, 45, 60, 88, 49, 100] <br> B) [78, 92, 60, 88, 100] <br> C) (78, 92, 60, 88, 100) <br> D) [50, 60, 88, 100] | **[78, 92, 60, 88, 100]** |
| 12 | `passed = [78, 92, 60, 88, 100]` <br> `bonus_marks = [min(m+5, 100) for m in passed]` <br> What does `bonus_marks` contain? | A) [83, 97, 65, 93, 105] <br> B) [78, 92, 60, 88, 100] <br> C) [83, 97, 65, 93, 100] <br> D) (83, 97, 65, 93, 100) | **[83, 97, 65, 93, 100]** |
| 13 | What is the type of `final_scores`? <br> `final_scores = tuple(bonus_marks)` | A) List <br> B) Set <br> C) Dictionary <br> D) Tuple | **Tuple** |
| 14 | What is the output of: <br> `indexed_scores = [(i, final_scores[i]) for i in range(len(final_scores))]` <br> `print(indexed_scores[2])` | A) (2, 97) <br> B) (1, 97) <br> C) (2, 65) <br> D) 65 | **(2, 65)** |
| 15 | What happens if the following line is executed? <br> `final_scores[0] = 90` | A) The value updates successfully <br> B) The tuple converts into a list <br> C) A runtime error occurs <br> D) Only the first element changes | **A runtime error occurs** |

-----
