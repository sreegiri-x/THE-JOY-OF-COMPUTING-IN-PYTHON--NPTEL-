# Solution: Dice Roller (Week 8, Programming Problem 2)

import random

rolls = [random.randint(1, 6) for _ in range(10)]
print("Dice rolls:", rolls)

most_frequent = max(set(rolls), key=rolls.count)
print(f"Most frequent outcome: {most_frequent} (appeared {rolls.count(most_frequent)} times)")
