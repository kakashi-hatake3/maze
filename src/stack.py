class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.insert(0, item)

    def empty(self):
        return len(self.stack) == 0

    def top(self):
        return self.stack[0]

    def size(self):
        return len(self.stack)

    def pop(self):
        return self.stack.pop(0) if not self.empty() else None
