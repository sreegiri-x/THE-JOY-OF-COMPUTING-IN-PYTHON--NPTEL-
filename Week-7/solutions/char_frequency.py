# Solution: Character Frequency (Week 7, Programming Problem 3)

s = input("Enter a string: ")
char_count = {}
for ch in s:
    char_count[ch] = char_count.get(ch, 0) + 1

print("Character frequencies:")
for ch, count in char_count.items():
    print(f"  '{ch}': {count}")
