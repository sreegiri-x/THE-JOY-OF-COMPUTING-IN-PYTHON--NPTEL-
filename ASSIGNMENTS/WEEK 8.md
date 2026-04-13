

# The Joy of Computing using Python
## Unit 11 - Week 8

### A Month of Chance - Simulating a Lottery Strategy

**Background**
Ravi, a college student interested in probability and data analysis, wants to understand whether playing a simple lottery-style game every day can be profitable in the long run. Instead of relying on intuition or anecdotes, he decides to simulate the experience using Python.

Ravi chooses a very straightforward strategy:
* Every day, he selects one fixed number between 1 and 10 as his bet.
* A system randomly draws a number between 1 and 10.
* If his chosen number matches the draw, he earns a large reward.
* If it doesn't, he incurs a small loss.

He repeats this experiment once per day for 30 days, representing a month of consistent participation.

**Objective of the Study**
The purpose of this case study is to:
* Observe how randomness affects outcomes over time
* Track profit and loss trends instead of isolated wins
* Visually analyze whether consistency in betting leads to gains or losses

Rather than focusing on a single lucky or unlucky day, Ravi wants to see the overall trajectory of his account balance.

**Experimental Setup**
* Ravi starts with an account balance of ₹0
* He plays the game once per day for 30 days
* Each day's result updates his account balance
* The balance is recorded daily to study trends over time

To make the results more intuitive, Ravi plots:
* Days (1-30) on the x-axis
* Account balance on the y-axis

This allows him to clearly see fluctuations, streaks of loss, occasional jumps, and the final outcome.

### Given Code for Analysis
Students are provided with the following Python code and are expected to analyze its behavior, output, and implications based on the case study above:

```python
import random
import matplotlib.pyplot as plt

# User Input
bet = int(input("Enter your bet from 1 to 10: "))

# Account initialization
account = 0

# Simulation loop for one month (30 days)
x = [] # Days
y = [] # Account balances

for day in range(30):
    lucky_draw = random.randint(1, 10)
    if bet == lucky_draw:
        account += 900
    else:
        account -= 100
    x.append(day + 1)
    y.append(account)

# Visualization
plt.plot(x, y)
plt.xlabel("Days")
plt.ylabel("Account Balance")
plt.title("Lottery Simulation Profit or Loss")
plt.show()
```

---

### Quiz: Week 8 Assignment 8

**1) What does the variable bet represent in the simulation?**
- The amount of money invested each day
- The randomly generated lucky number
- The fixed number chosen by the user for the entire month
- The number of days the simulation runs

**Correct Answer:** The fixed number chosen by the user for the entire month

**2) How many times is the lottery game simulated in the program?**
- 10
- 30
- Until the user wins
- Depends on the bet value

**Correct Answer:** 30

**3) What happens to the account balance when the bet does NOT match the lucky draw?**
- It remains unchanged
- It increases by 100
- It decreases by 900
- It decreases by 100

**Correct Answer:** It decreases by 100

**4) Which Python library is responsible for generating randomness in the simulation?**
- matplotlib
- random
- pyplot
- math

**Correct Answer:** random

**5) What do the lists x and y store respectively?**
- Account balances and days
- Bets and lucky numbers
- Days and account balances
- Wins and losses

**Correct Answer:** Days and account balances

**6) If the user never wins even once during the 30 days, what will be the final account balance?**
- -3000
- -900
- -100
- 0

**Correct Answer:** -3000

**7) What is the probability of winning on any single day?**
- 1/30
- 1/100
- 1/10
- Depends on previous days

**Correct Answer:** 1/10

**8) Why does the account balance graph typically show long downward trends with occasional sharp upward jumps?**
- Because the bet value changes daily
- Because losses are frequent and wins are rare but large
- Because matplotlib smooths the curve
- Because account balance is averaged

**Correct Answer:** Because losses are frequent and wins are rare but large

**9) Which change would make the simulation more statistically reliable without changing the game rules?**
- Increasing the win amount
- Running the simulation for more days
- Changing the bet every day
- Removing the plot

**Correct Answer:** Running the simulation for more days

**10) Despite a high winning reward (900), why does the simulation still tend to show losses over time?**
- Because the plotting scale is incorrect
- Because the probability of winning is too low compared to the loss frequency
- Because Python integers overflow
- Because the account starts at zero

**Correct Answer:** Because the probability of winning is too low compared to the loss frequency

---

### Detecting Pattern Consistency Between Two Strings

**Background**
A software team working on a text pattern-matching system needs to verify whether two given strings follow the same structural pattern. This requirement arises in areas such as:
* Data normalization
* Search indexing
* Language processing
* Pattern validation in user input

**Problem Scenario**
Two strings are given:
* String S represents an original pattern
* String T represents a transformed version

The task is to determine whether:
* Each character in S consistently maps to one unique character in T
* The mapping is one-to-one and reversible
* The relative structure of both strings remains identical

**Example:**
* "egg" and "add" follow the same pattern
* "foo" and "bar" do not

**Constraints of the Study**
* Both strings must be of equal length
* A character cannot map to multiple different characters
* Two different characters cannot map to the same character
* The comparison is performed position by position

### Given Code for Analysis

```python
def isomorphicString(s, t):
    if len(s) != len(t):
        return False
    
    s_map = {}
    t_map = {}
    
    for i in range(len(s)):
        char_s = s[i]
        char_t = t[i]
        
        if (char_s in s_map and s_map[char_s] != char_t) or \
           (char_t in t_map and t_map[char_t] != char_s):
            return False
            
        s_map[char_s] = char_t
        t_map[char_t] = char_s
        
    return True
```

**11) What will the function return for s="egg" and t="add"?**
- True
- False
- Depends on dictionary insertion order
- Raises an error

**Correct Answer:** True

**12) What is the first condition that can cause the function to return False?**
- Duplicate characters in s
- Conflicting mappings in dictionaries
- Repeated characters at adjacent positions
- Length mismatch between the two strings

**Correct Answer:** Length mismatch between the two strings

**13) What will the function return for s="ab" and t="cc"?**
- False
- True
- Only the forward mapping fails
- Depends on loop iteration

**Correct Answer:** False

**14) Why is the condition checking both s_map and t_map necessary?**
- To reduce memory usage
- To avoid nested loops
- To speed up execution
- To enforce a one-to-one and reversible character mapping

**Correct Answer:** To enforce a one-to-one and reversible character mapping

**15) Which of the following best describes what the algorithm is verifying?**
- Structural equivalence between two strings
- Lexicographical ordering
- Equality of character frequencies
- Whether both strings are permutations

**Correct Answer:** Structural equivalence between two strings

---
