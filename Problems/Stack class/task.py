class Stack:

    def __init__(self):
        self.items = []

    def push(self, el):
        self.items.append(el)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def is_empty(self):
        return self.items == []
