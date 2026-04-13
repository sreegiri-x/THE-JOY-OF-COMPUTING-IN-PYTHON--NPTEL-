
# The Joy of Computing using Python - Unit 7 - Week 4

## Building a Mini Dobble Game Using Python
In this activity, a learner designs a simplified version of the popular Dobble game using Python. The goal of the game is simple: two cards are generated such that exactly one symbol is common between them, and the player must correctly identify that common symbol.

### Step 1: Preparing the Symbol Set
The game begins by importing two built-in Python modules:
* **string**: used to access alphabets easily.
* **random**: used to generate randomness in the game.

Using `string.ascii_letters`, a list of symbols is created that contains:
* lowercase letters (a-z)
* uppercase letters (A-Z)

This list becomes the symbol pool from which all card symbols are drawn. Once a symbol is used, it is removed from the pool to prevent duplication.

### Step 2: Deciding Positions on Cards
Each card contains 5 positions, indexed from 0 to 4. Two random positions are generated:
* **pos1**: where the common symbol will appear on Card 1.
* **pos2**: where the common symbol will appear on Card 2.

These positions are chosen randomly, which ensures that the common symbol does not always appear in the same place.

### Step 3: Selecting the Common Symbol
One symbol is randomly selected from the symbol pool to act as the common symbol shared by both cards. Immediately after selecting it, the symbol is removed from the pool, ensuring:
* It cannot accidentally appear again.
* Uniqueness across the rest of the cards.

### Step 4: Creating the Cards
Two lists are created: `card1` and `card2`. Each list has 5 empty slots, initialized with **ZERO**. These lists represent the two cards shown to the player.

### Step 5: Handling Common and Non-Common Positions
* If `pos1` and `pos2` are the same, the common symbol is placed at that index in both cards.
* If they are different:
    * The common symbol is placed at `pos1` in Card 1.
    * The same symbol is placed at `pos2` in Card 2.
    * Two different symbols are placed in the swapped positions to avoid accidental matching.

### Step 6: Filling Remaining Positions Using a Loop
A `while` loop runs from index 0 to 4. For every index except `pos1` and `pos2`:
* One new symbol is picked for Card 1.
* A different new symbol is picked for Card 2.
* Both symbols are removed from the pool.

---

## Quiz: Week 4 Assignment

**1) What is the maximum number of unique symbols that can be safely used by this program without causing a runtime error?**
* 26
* 52
* 10
* Unlimited  
**Accepted Answer:** 52

**2) Which statement about pos1 and pos2 is logically correct?**
* They may or may not be equal
* They are always different
* They are fixed once generated
* They cannot be equal  
**Accepted Answer:** They may or may not be equal

**3) Why is same_symbol removed from the symbol list immediately after selection?**
* To improve randomness
* To reduce memory usage
* To ensure it appears exactly once on each card
* To simplify the loop condition  
**Accepted Answer:** To ensure it appears exactly once on each card

**4) What problem does the condition if pos1 == pos2 prevent?**
* Index out-of-range error
* Logical conflict in symbol placement
* Infinite looping
* Input mismatch  
**Accepted Answer:** Logical conflict in symbol placement

**5) When pos1 != pos2, how many times does the while loop assign symbols?**
* 5
* 2
* 4
* 3  
**Accepted Answer:** 3

**6) What is the most serious consequence if symbols are not removed inside the loop?**
* Cards become sorted automatically
* Multiple common symbols may appear
* Loop runs indefinitely
* Cards become identical  
**Accepted Answer:** Multiple common symbols may appear

**7) Which player input would be marked incorrect even if the symbol looks correct?**
* Input entered quickly
* Input with correct spacing
* Lowercase input for an uppercase symbol
* Input after a delay  
**Accepted Answer:** Lowercase input for an uppercase symbol

**8) Which statement is guaranteed true every time the program runs?**
* Symbols appear in alphabetical order
* Both cards are mirror images
* Cards share no symbols
* Cards share exactly one symbol  
**Accepted Answer:** Cards share exactly one symbol

---

## Case Study: List Assignment and Copying

### Question 9
```python
a = [10, 20, 30]
b = a
b.append(40)
print(a)
```
* [10, 20, 30]
* [10, 20, 30, 40]
* Error
* [40]  
**Accepted Answer:** [10, 20, 30, 40]

### Question 10
```python
a = [1, 2, 3]
b = a.copy()
b[0] = 99
print(a)
```
* [1, 99, 3]
* [99, 2, 3]
* [1, 2, 3]
* Error  
**Accepted Answer:** [1, 2, 3]

### Question 11
```python
a = [[1, 2], [3, 4]]
b = a.copy()
b[0][1] = 99
print(a)
```
* Error
* [[1, 2], [3, 4]]
* [[1, 2], [3, 99]]
* [[1, 99], [3, 4]]  
**Accepted Answer:** [[1, 99], [3, 4]]

### Question 12
```python
a = [[5, 6], [7, 8]]
b = a[:]
b[1] = [0, 0]
print(a)
```
* Error
* [[5, 6], [7, 8]]
* [[5, 6], [0, 0]]
* [[0, 0], [7, 8]]  
**Accepted Answer:** [[5, 6], [7, 8]]

### Question 13
```python
a = [[5, 6], [7, 8]]
b = a[:]
b[1][0] = 100
print(a)
```
* [[5, 6], [7, 8]]
* Error
* [[100, 6], [7, 8]]
* [[5, 6], [100, 8]]  
**Accepted Answer:** [[5, 6], [100, 8]]

### Question 14
```python
import copy
a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)
b[0][0] = 9
print(a)
```
* [[9, 2], [3, 4]]
* Error
* [[1, 2], [3, 4]]
* [[1, 9], [3, 4]]  
**Accepted Answer:** [[1, 2], [3, 4]]

### Question 15
```python
import copy
a = [[1, 2], [3, 4]]
b = a
c = a.copy()
d = copy.deepcopy(a)
b[0][0] = 10
c[1][1] = 20
d[0][1] = 30
print(a)
```
* [[10, 30], [3, 20]]
* [[10, 2], [3, 4]]
* [[1, 2], [3, 4]]
* [[10, 2], [3, 20]]  
**Accepted Answer:** [[10, 2], [3, 20]]

---
