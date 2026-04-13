# Week 12 — Projects and Applications

## Assignment Questions

---

### Q1. What is a **stack** data structure?

- A) First In, First Out (FIFO)
- B) Last In, First Out (LIFO)
- C) A sorted list
- D) A key-value store

---

### Q2. What is a **queue** data structure?

- A) Last In, First Out (LIFO)
- B) First In, First Out (FIFO)
- C) A sorted list
- D) A tree structure

---

### Q3. What does `list.pop()` do when used as a stack operation?

- A) Adds an element to the front
- B) Removes and returns the last element (top of stack)
- C) Returns the first element
- D) Sorts the stack

---

### Q4. Which of the following best describes **object-oriented programming (OOP)**?

- A) Writing functions that call each other
- B) Organizing code around objects that combine data and behavior
- C) Writing all code in a single file
- D) Using only built-in Python functions

---

### Q5. What is a Python **class**?

- A) A function that returns a value
- B) A blueprint for creating objects
- C) A type of list
- D) A way to import modules

---

### Q6. What does the `__init__` method do in a class?

- A) Destroys the object
- B) Initializes object attributes when an instance is created
- C) Defines class-level constants
- D) Imports external modules

---

### Q7. What is the output of the following?

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says hello!"

a = Animal("Dog")
print(a.speak())
```

- A) `Animal says hello!`
- B) `Dog says hello!`
- C) `hello!`
- D) `Error`

---

### Q8. What is **inheritance** in OOP?

- A) Hiding implementation details
- B) A class acquiring properties and methods of another class
- C) Creating multiple objects from one class
- D) Overloading operators

---

### Q9. What is the purpose of `self` in a Python class?

- A) It refers to the class itself
- B) It refers to the current instance of the class
- C) It is a keyword that must be used in all functions
- D) It refers to the parent class

---

### Q10. What does the following code print?

```python
class Counter:
    count = 0

    def increment(self):
        Counter.count += 1

c1 = Counter()
c2 = Counter()
c1.increment()
c2.increment()
print(Counter.count)
```

- A) `0`
- B) `1`
- C) `2`
- D) `Error`

---

### Programming Problem 1

Implement a **Stack** class in Python with `push`, `pop`, `peek`, and `is_empty` methods.

---

### Programming Problem 2

Create a Python class `BankAccount` with:
- Attributes: `owner` (name) and `balance`
- Methods: `deposit(amount)`, `withdraw(amount)`, and `get_balance()`
- `withdraw` should print an error if there are insufficient funds.

---

### Programming Problem 3

Write a Python program to simulate a simple **number guessing game**: the program generates a random number between 1 and 100, and the user keeps guessing until they get it right (with "Too high" / "Too low" hints).
