# Solution: Word Count in File (Week 8, Programming Problem 3)

filename = input("Enter the filename: ")
try:
    with open(filename, "r") as f:
        content = f.read()
    words = content.split()
    print(f"Total words in '{filename}': {len(words)}")
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
