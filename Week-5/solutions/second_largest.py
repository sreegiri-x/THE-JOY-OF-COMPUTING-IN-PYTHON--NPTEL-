# Solution: Second Largest Element (Week 5, Programming Problem 1)

n = int(input("How many elements? "))
lst = []
for i in range(n):
    lst.append(int(input(f"Enter element {i+1}: ")))

lst_sorted = sorted(set(lst))
if len(lst_sorted) >= 2:
    print(f"Second largest: {lst_sorted[-2]}")
else:
    print("Not enough distinct elements")
