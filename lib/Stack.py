class Stack:

    def __init__(self, items=None, limit=100):
        if items is None:
            self.items = []
        else:
            self.items = items
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if not self.full():
            self.items.append(item)
        # If full, do not raise error, just ignore the push

    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

    def full(self):
        return self.size() >= self.limit

    def search(self, target):
        if target not in self.items:
            return -1
        # Distance from top: top is last element, index -1
        # So distance = size - 1 - index of target
        index = self.items.index(target)
        return self.size() - 1 - index
