# Solution: Student with Highest Marks (Week 7, Programming Problem 1)

students = {
    "Alice": 88,
    "Bob": 72,
    "Charlie": 95,
    "Diana": 80,
    "Eve": 91
}

top_student = max(students, key=students.get)
print(f"Student with highest marks: {top_student} ({students[top_student]})")
