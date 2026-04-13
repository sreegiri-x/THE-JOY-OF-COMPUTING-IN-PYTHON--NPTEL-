# Solution: Count Vowels (Week 6, Programming Problem 1)

sentence = input("Enter a sentence: ")
vowels = "aeiouAEIOU"
count = sum(1 for ch in sentence if ch in vowels)
print(f"Number of vowels: {count}")
