# Solution: Student Marks Bar Chart (Week 11, Programming Problem 3)

import matplotlib.pyplot as plt

students = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
marks = [85, 72, 95, 60, 88]

plt.bar(students, marks, color=["blue", "green", "red", "purple", "orange"])
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.ylim(0, 100)
plt.tight_layout()
plt.savefig("student_marks.png")
plt.show()
