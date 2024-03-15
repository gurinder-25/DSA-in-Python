class stack:
    def __init__(self):
        self.stack = []
    def push(self, val):
        self.stack.append(val)
    def pop(self):
        return self.stack.pop()

s = stack()
s.push(3)
s.push(2)
s.push(1)
print(s.pop())
print(s.pop())
print(s.pop())