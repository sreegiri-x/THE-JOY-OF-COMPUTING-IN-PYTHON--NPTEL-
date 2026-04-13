# Solution: Bubble Sort (Week 10, Programming Problem 1)

def bubble_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Sorted:", bubble_sort(numbers))
