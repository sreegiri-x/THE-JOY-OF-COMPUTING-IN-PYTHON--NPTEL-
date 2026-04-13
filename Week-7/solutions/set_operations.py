# Solution: Set Operations (Week 7, Programming Problem 2)

a = set(map(int, input("Enter elements of set A separated by spaces: ").split()))
b = set(map(int, input("Enter elements of set B separated by spaces: ").split()))

print(f"Union: {a | b}")
print(f"Intersection: {a & b}")
print(f"Difference (A - B): {a - b}")
