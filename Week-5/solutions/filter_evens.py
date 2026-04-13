# Solution: Filter Even Numbers (Week 5, Programming Problem 2)

def get_evens(numbers):
    return [x for x in numbers if x % 2 == 0]

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Even numbers:", get_evens(numbers))
