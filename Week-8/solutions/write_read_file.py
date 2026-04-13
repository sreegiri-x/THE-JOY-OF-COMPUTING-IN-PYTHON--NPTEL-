# Solution: Write and Read File (Week 8, Programming Problem 1)

# Write numbers 1-10 to file
with open("numbers.txt", "w") as f:
    for i in range(1, 11):
        f.write(f"{i}\n")

# Read and print the file
print("File contents:")
with open("numbers.txt", "r") as f:
    print(f.read())
