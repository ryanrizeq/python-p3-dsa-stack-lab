class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = []
        self.limit = limit
        for item in items:
            self.items.append(item)

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        if (not self.full()):
            self.items.append(item)
        else:
            return None

    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()

    def peek(self):
        pass
    
    def size(self):
        return len(self.items)

    def full(self):
        if (len(self.items) >= self.limit):
            return True
        return False

    def search(self, target):
        count = len(self.items) - 1
        for item in self.items:
            if item == target:
                return count
            count -= 1
        return -1
