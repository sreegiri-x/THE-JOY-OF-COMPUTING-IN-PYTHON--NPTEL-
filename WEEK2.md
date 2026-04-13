
---

# The Joy of Computing using Python
## Unit 5 - Week 2: Assignment 2

### Ravi's Nested Loop Implementation
Ravi is asked to print the following pattern using Python:
1
22
333
4444
55555

He knows that a single loop controls the number of lines, so he decides to use nested `for` loops. Ravi writes the following code:

```python
for i in range(1, 6):
    for j in range(1, i):
        print(i)
```

The code runs without errors and prints multiple values on the screen. Ravi assumes that because the inner loop runs multiple times, the digit will automatically appear the required number of times on the same line. However, when the output is observed, the pattern does not match the required format.

The instructor uses Ravi's code as a learning case. Learners are expected to analyze how the outer loop controls the number of rows, how the inner loop controls repetition, and why the current placement of the `print()` statement leads to an incorrect output format.

---

#### 1) How many times does the outer loop execute?
* 4
* 5
* 6
* Depends on the inner loop

**Answer:** 5

---

#### 2) Why does Ravi's code print each number on a new line instead of the same line?
* Because `print()` moves the cursor to the next line by default
* Because `range()` creates new lines.
* Because the inner loop executes first
* Because nested loops cannot print patterns

**Answer:** Because `print()` moves the cursor to the next line by default

---

#### 3) Ravi's program executes without errors but fails to produce the required pattern. Which of the following best explains the cause?
* The outer loop does not include the final value required for printing the last line
* The inner loop variable is declared but not explicitly used in the print statement
* The print statement is placed inside the inner loop instead of after it
* The inner loop executes one fewer iteration than required for each value of i

**Answer:** The inner loop executes one fewer iteration than required for each value of i

---

#### 4) After correcting the inner loop to execute the required number of times, Ravi observes that the digits are still printed on separate lines. Which change is necessary to ensure that each digit appears on the same line before moving to the next line?
* Replace `print(i)` with `print()` inside the inner loop
* Move the `print(i)` statement outside the inner loop
* Add an empty `print()` statement at the beginning of the outer loop
* Modify the print statement to suppress the default newline character

**Answer:** Modify the print statement to suppress the default newline character

---

#### 5) In the corrected nested-loop program, why is an additional `print()` statement required immediately after the inner loop completes?
* To move the cursor to the next line after printing all digits for the current value of i
* To reset the value of the loop variable before the next iteration begins
* To ensure the inner loop terminates before the outer loop continues
* To prevent the digits printed in different iterations from overlapping

**Answer:** To move the cursor to the next line after printing all digits for the current value of i

---

#### 6) Which of the following Python code snippets correctly produces the required output?
```python
# Option A
for i in range(1, 6):
    for j in range(1, i):
        print(i, end="")
    print()

# Option B
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# Option C
for i in range(1, 6):
    print(i)
    for j in range(1, i):
        print(i, end="\n")

# Option D
for i in range(1, 6):
    for j in range(1, i + 1):
        print(i, end="")
    print()
```

**Answer:**
```python
for i in range(1, 6):
    for j in range(1, i + 1):
        print(i, end="")
    print()
```

---

### Palindrome Number Checker in Python
Ravi is learning Python and is currently practicing loops and arithmetic operations. As part of his practice, he is given a task to check whether a given number is a palindrome.

**Examples:**
* 121: Palindrome
* 456: Not a Palindrome

Ravi decides not to convert the number into a string because he wants to strengthen his understanding of:
* `while` loops
* Modulus (`%`) operator
* Integer division (`//`)

```python
def is_palindrome(n):
    original = n
    reverse = 0
    while n > 0:
        reverse = reverse * 10 + (n % 10)
        n //= 10
    return reverse == original
```

---

#### 7) What is the final value of reverse when the function is called as: `is_palindrome(120)`?
* 210
* 120
* 21
* 12

**Answer:** 21

---

#### 8) What will the function return for the input: `is_palindrome(7)`?
* Error because loop runs only once
* True
* False
* None

**Answer:** True

---

#### 9) How many times does the while loop execute when the function is called as: `is_palindrome(1001)`?
* 2
* 4
* 3
* 1

**Answer:** 4

---

#### 10) Suppose the loop condition is changed to: `while n >= 0:`. What will happen when the function is called with `is_palindrome(5)`?
* It enters an infinite loop
* It returns False after one iteration
* It correctly returns True
* It raises a runtime error

**Answer:** It enters an infinite loop

---

### Smart Discount Calculator
A retail store introduces a Smart Discount Calculator to ensure that discounts are applied in a consistent and predictable manner.

**1. Purchase Amount Based Discount**
* Purchase amount < 1,000: no discount is applied.
* Purchase amount >= 1,000: a 10% purchase-based discount becomes eligible.

**2. Customer Type Based Discount**
* Regular Customer: no customer-type discount is considered.
* Premium Customer:
    * If purchase amount < 2,000: premium discount is ignored.
    * If purchase amount >= 2,000: a 5% premium discount becomes eligible.

**3. Final Discount Selection Rule**
* If no discount is eligible: final payable amount equals the purchase amount.
* If exactly one discount is eligible: that discount is applied.
* If both are eligible: apply only the one that results in the higher benefit.
* **Note: Both discounts are never applied together.**

---

#### 11) A customer is a regular customer and makes a purchase of ₹850. Which code fragment correctly represents the discount logic applied by the calculator?
**Answer:**
```python
discount = 0
if amount >= 1000:
    discount = amount * 0.10
```

---

#### 12) A premium customer makes a purchase of ₹1,500. Which discount will the system finally apply?
* 5% premium discount
* No discount
* 10% purchase-based discount
* Both 10% and 5% discounts

**Answer:** 10% purchase-based discount

---

#### 13) A premium customer makes a purchase of ₹2,500. Which logic ensures that only one discount is applied?
**Answer:** `discount = max(amount * 0.10, amount * 0.05)`

---

#### 14) A premium customer makes a purchase of ₹2,000 exactly. Which discount amount is applied?
* ₹100
* ₹200
* ₹300
* ₹0

**Answer:** ₹200

---

#### 15) A premium customer makes a purchase of ₹1,800. Which of the following code fragments correctly produces the discount applied by the Smart Discount Calculator?
**Answer:**
```python
if premium and amount >= 2000:
    discount = amount * 0.05
elif amount >= 1000:
    discount = amount * 0.10
```

---
