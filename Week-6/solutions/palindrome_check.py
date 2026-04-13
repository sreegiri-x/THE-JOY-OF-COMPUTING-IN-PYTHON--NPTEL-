# Solution: Palindrome Check (Week 6, Programming Problem 2)

s = input("Enter a string: ").lower().replace(" ", "")
if s == s[::-1]:
    print(f'"{s}" is a Palindrome')
else:
    print(f'"{s}" is NOT a Palindrome')
