# Solution: Stack Class (Week 12, Programming Problem 1)

class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if self.is_empty():
            print("Stack is empty!")
            return None
        return self._data.pop()

    def peek(self):
        if self.is_empty():
            print("Stack is empty!")
            return None
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0


# Test
s = Stack()
s.push(10)
s.push(20)
s.push(30)
print("Top:", s.peek())   # 30
print("Pop:", s.pop())    # 30
print("Top:", s.peek())   # 20
