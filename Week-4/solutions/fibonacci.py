# Solution: Fibonacci (Week 4, Programming Problem 2)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Print first 8 Fibonacci numbers
for i in range(8):
    print(fibonacci(i), end=" ")
print()
