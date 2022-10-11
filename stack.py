class Stack:
    
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return not self.items

    def size(self):
        return len(self.items)

    # Defines what the 'print' statement does with the class
    def __str__(self):
        return str(self.items)


if __name__ == "__main__":
    s = Stack()
    print(s)
    print(s.is_empty())
    s.push(15)
    print(s)
    s.push(3)
    s.push(26)
    print(s)
    print(s.pop())
    print(s)
    print(s.peek())
    print(s)
    print(s.size())