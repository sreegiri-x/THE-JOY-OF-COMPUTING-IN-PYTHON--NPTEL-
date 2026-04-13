# Week 11 — Data Visualization and Turtle Graphics: Answers

---

### Q1. Answer: **C) `turtle`**

Python's built-in `turtle` module provides turtle graphics capabilities.

---

### Q2. Answer: **B) Moves the turtle forward 100 units**

`t.forward(100)` (or `t.fd(100)`) moves the turtle in its current direction by 100 units, drawing a line if the pen is down.

---

### Q3. Answer: **B) Rotates the turtle 90 degrees clockwise**

`t.right(angle)` turns the turtle clockwise. `t.left(angle)` turns counterclockwise.

---

### Q4. Answer: **B) Repeat `forward(100)` and `right(90)` 4 times**

A square has 4 equal sides with 90-degree turns:
```python
for _ in range(4):
    t.forward(100)
    t.right(90)
```

---

### Q5. Answer: **B) Keeps the turtle window open until the user closes it**

`turtle.done()` starts the event loop and prevents the window from closing immediately when the script finishes.

---

### Q6. Answer: **A) `t.color("red")`**

`t.color()` sets both the pen color and fill color. `t.pencolor("red")` sets only the pen color.

---

### Q7. Answer: **C) `matplotlib`**

`matplotlib` is the most widely used Python library for data visualization (line plots, bar charts, histograms, etc.).

---

### Q8. Answer: **C) Displays the plot**

`plt.show()` renders and displays the figure in an interactive window.

---

### Q9. Answer: **B) Lifts the pen so the turtle moves without drawing**

`penup()` (or `pu()`) lifts the pen — the turtle moves but does not draw. `pendown()` lowers the pen again.

---

### Q10. Answer: **C) `t.circle(50)`**

`t.circle(radius)` draws a circle with the given radius.

---

## Programming Problem 1 — Solution: Hexagon

```python
import turtle

t = turtle.Turtle()
t.speed(3)

for _ in range(6):
    t.forward(100)
    t.right(60)   # 360 / 6 = 60 degrees

turtle.done()
```

---

## Programming Problem 2 — Solution: Star

```python
import turtle

t = turtle.Turtle()
t.speed(3)
t.color("red")

for _ in range(5):
    t.forward(150)
    t.right(144)   # exterior angle of a 5-pointed star

turtle.done()
```

---

## Programming Problem 3 — Solution: Bar Chart

```python
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
```
