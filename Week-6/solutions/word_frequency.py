# Solution: Word Frequency Counter (Week 6, Programming Problem 3)

sentence = input("Enter a sentence: ").lower()
words = sentence.split()
frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("Word frequencies:")
for word, count in frequency.items():
    print(f"  {word}: {count}")
