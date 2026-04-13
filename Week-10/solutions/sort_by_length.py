# Solution: Sort Words by Length (Week 10, Programming Problem 3)

words = input("Enter words separated by spaces: ").split()
words.sort(key=len)
print("Sorted by length:", words)
