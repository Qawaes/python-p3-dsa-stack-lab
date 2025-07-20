class Stack:

    def __init__(self, items=None, limit=100):
        if items is None:
            self.items = []
        else:
            self.items = items[:limit]  # Truncate initial items if over limit
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0
    
    def push(self, item):
      if self.size() < self.limit:
        self.items.append(item)

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
        """
        Returns 0-based distance from top of stack to target if found.
        Returns -1 if not found.
        """
        try:
            index = len(self.items) - 1 - self.items[::-1].index(target)
            return len(self.items) - 1 - index
        except ValueError:
            return -1
