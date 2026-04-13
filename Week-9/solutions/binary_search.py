# Solution: Binary Search (Week 9, Programming Problem 3)

def binary_search(lst, target):
    low, high = 0, len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

lst = sorted([4, 2, 7, 1, 9, 3])
print("Sorted list:", lst)
target = int(input("Enter target: "))
index = binary_search(lst, target)
if index != -1:
    print(f"Found at index {index}")
else:
    print("Not found")
