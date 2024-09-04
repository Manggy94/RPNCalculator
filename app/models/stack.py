class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def clear(self):
        self.items = []

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def get_items(self):
        return self.items

    def size(self):
        return len(self.items)

    def add(self):
        if self.size() < 2:
            return None
        a = self.pop()
        b = self.pop()
        self.push(b + a)

    def subtract(self):
        if self.size() < 2:
            return None
        a = self.pop()
        b = self.pop()
        self.push(b - a)

    def multiply(self):
        if self.size() < 2:
            return None
        a = self.pop()
        b = self.pop()
        self.push(b * a)

    def divide(self):
        if self.size() < 2:
            return None
        a = self.pop()
        b = self.pop()
        if a == 0:
            return None
        self.push(b / a)


