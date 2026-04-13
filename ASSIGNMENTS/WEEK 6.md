
# The Joy of Computing using Python
## Unit 9 - Week 6: Assignment 6

### In-Place Data Reversal in a Memory-Constrained System

**Context**
A learning analytics platform maintains a list of numerical records representing student interaction order. To save memory, the system must reverse these records in-place.

**System Constraints**
* The reversal must happen within the same list (no new list allowed).
* The solution must be function-based.
* The team prefers recursive approaches for internal training.
* The system must handle empty, odd-length, and even-length lists.

**Implementation Provided**
```python
def reverseArray (nums):
    start = 0
    end = len(nums)-1
    swap = 0
    return helper_reverse(start, end, nums, swap)

def helper_reverse(start, end, nums, swap):
    if start > end:
        return nums
    swap = nums[start]
    nums[start] = nums[end]
    nums[end] = swap
    return helper_reverse(start + 1, end - 1, nums, swap)
```

---

### Questions & Options (Section 1)

**1) If the function `reverseArray` is called with the input: `nums = [1, 2, 3, 4]`, what will be the final value of `nums`?**
* [1, 2, 3, 4]
* [4, 3, 2, 1]
* [2, 1, 4, 3]
* [4, 2, 3, 1]
**Accepted Answer:**
[4, 3, 2, 1]

**2) For which condition does the recursive process stop?**
* When start == end
* When start > end
* When end == 0
* When swap becomes zero
**Accepted Answer:**
When start > end

**3) What does the function `reverseArray (nums)` return?**
* The modified list nums
* None
* A new reversed list
* Only the last swapped value
**Accepted Answer:**
The modified list nums

**4) What happens when the input list has an odd number of elements?**
* The middle element is removed
* The program crashes
* The middle element remains unchanged
* The middle element is swapped with itself twice
**Accepted Answer:**
The middle element remains unchanged

**5) What is the output when `reverseArray ([])` is executed?**
* Runtime error
* None
* [0]
* 0
**Accepted Answer:**
0

**6) What is the extra space complexity of this approach (excluding input list)?**
* $O(n)$ due to recursion stack
* $O(1)$
* $O(log\ n)$
* $O(n^2)$
**Accepted Answer:**
$O(n)$ due to recursion stack

**7) What is the actual role of the variable `swap`?**
* It stores recursion depth
* It temporarily holds a value during exchange
* It controls termination
* It accumulates reversed values
**Accepted Answer:**
It temporarily holds a value during exchange

**8) For a list of length 6, how many recursive calls perform swaps?**
* 6
* 4
* 3
* 5
**Accepted Answer:**
3

**9) Which statement best describes the behavior of this function?**
* It creates and returns a new list
* It modifies the list but returns nothing
* It uses iteration internally
* It mutates the original list and returns it
**Accepted Answer:**
It mutates the original list and returns it

**10) If the final `return helper_reverse(...)` line is removed from `helper_reverse`, what happens?**
* The list still gets reversed but None is returned
* The list is not reversed
* The program throws a syntax error
* Only the first swap happens
**Accepted Answer:**
Only the first swap happens

---

### Terminal-Based Tic Tac Toe Game

**11) When the program starts executing and no input has been entered yet, which of the following is true?**
* The board is displayed with all cells filled with "X"
* The board is displayed with all cells empty
* The game immediately asks Player O for input
* The game prints "It's a draw!"
**Accepted Answer:**
The board is displayed with all cells empty

**12) A player enters the following input when prompted: `2`. What happens next?**
* The move is accepted and placed in column 2
* The program crashes with an error
* The program asks the player to re-enter input
* The turn switches to the next player
**Accepted Answer:**
The program asks the player to re-enter input

**13) Which situation causes the variable `turns` to increase by 1?**
* When the board is displayed
* When a player enters invalid input
* When a player overwrites an occupied cell
* When a valid move is successfully placed on the board
**Accepted Answer:**
When a valid move is successfully placed on the board

**14) The game stops immediately when which of the following occurs?**
* Nine turns have been completed
* A winning condition is detected
* An invalid move is entered
* The board is fully displayed
**Accepted Answer:**
A winning condition is detected

**15) Under which condition does the program print "It's a draw!"?**
* When Player O makes the last move
* When no diagonal matches are found
* When the loop ends without detecting a winner
* When all rows contain mixed symbols
**Accepted Answer:**
When the loop ends without detecting a winner

---

