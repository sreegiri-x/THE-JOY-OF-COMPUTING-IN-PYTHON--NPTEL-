# Solution: Linear Search (Week 9, Programming Problem 2)

def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1

lst = [4, 2, 7, 1, 9, 3]
target = int(input("Enter target: "))
index = linear_search(lst, target)
if index != -1:
    print(f"Found at index {index}")
else:
    print("Not found")
