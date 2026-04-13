# Solution: Selection Sort (Week 10, Programming Problem 2)

def selection_sort(lst):
    n = len(lst)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Sorted:", selection_sort(numbers))
