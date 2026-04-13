# Week 12 — Projects and Applications: Answers

---

### Q1. Answer: **B) Last In, First Out (LIFO)**

A stack is like a pile of plates — the last one placed on top is the first one removed.

---

### Q2. Answer: **B) First In, First Out (FIFO)**

A queue is like a line of people — the first one to join is the first one served.

---

### Q3. Answer: **B) Removes and returns the last element (top of stack)**

A Python list can be used as a stack: `append()` to push and `pop()` to pop from the top (last element).

---

### Q4. Answer: **B) Organizing code around objects that combine data and behavior**

OOP is a programming paradigm where programs are built around objects that encapsulate data (attributes) and behavior (methods).

---

### Q5. Answer: **B) A blueprint for creating objects**

A class defines the structure (attributes) and behavior (methods) that its instances (objects) will have.

---

### Q6. Answer: **B) Initializes object attributes when an instance is created**

`__init__` is the constructor method. It is automatically called when a new instance of the class is created.

---

### Q7. Answer: **B) Dog says hello!**

`a = Animal("Dog")` creates an instance with `self.name = "Dog"`. `a.speak()` returns `"Dog says hello!"`.

---

### Q8. Answer: **B) A class acquiring properties and methods of another class**

Inheritance allows a child class to reuse code from a parent class. Example: `class Dog(Animal):`.

---

### Q9. Answer: **B) It refers to the current instance of the class**

`self` is always the first parameter of instance methods. It allows methods to access and modify the instance's own attributes.

---

### Q10. Answer: **C) 2**

`Counter.count` is a class variable shared by all instances. Each call to `increment()` increases it by 1. After two calls, it equals `2`.

---

## Programming Problem 1 — Solution: Stack Class

```python
class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if self.is_empty():
            print("Stack is empty!")
            return None
        return self._data.pop()

    def peek(self):
        if self.is_empty():
            print("Stack is empty!")
            return None
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

# Test
s = Stack()
s.push(10)
s.push(20)
s.push(30)
print("Top:", s.peek())   # 30
print("Pop:", s.pop())    # 30
print("Top:", s.peek())   # 20
```

---

## Programming Problem 2 — Solution: BankAccount Class

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₹{amount}. New balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew ₹{amount}. New balance: ₹{self.balance}")

    def get_balance(self):
        return self.balance

# Test
account = BankAccount("Alice", 1000)
account.deposit(500)
account.withdraw(200)
account.withdraw(2000)
print(f"Balance: ₹{account.get_balance()}")
```

---

## Programming Problem 3 — Solution: Number Guessing Game

```python
import random

secret = random.randint(1, 100)
attempts = 0

print("Welcome! Guess the number between 1 and 100.")

while True:
    guess = int(input("Your guess: "))
    attempts += 1

    if guess < secret:
        print("Too low! Try again.")
    elif guess > secret:
        print("Too high! Try again.")
    else:
        print(f"Correct! You guessed it in {attempts} attempts.")
        break
```
