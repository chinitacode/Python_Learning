class Stack():
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items

s = Stack()
print(s.is_empty())
print(s.peek())
s.push('A')
s.push('B')
print(s.get_stack())
print(s.is_empty())
print(s.size())
print(s.peek())
