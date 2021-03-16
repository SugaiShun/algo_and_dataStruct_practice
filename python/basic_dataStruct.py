"""
スタックやキュートのデータ構造
"""

class stack:
    """
    original stack class.
    """
    def __init__(self):
        self.stack = []
    def push(self,item):
        return self.stack.append(item)
    def pop(self):
        return self.stack.pop()
    def is_empty(self):
        return self.stack==[]
    def size(self):
        return len(self.stack)
    def top(self):
        return self.stack[-1]

class queue:
    """
    original queue class.
    """
    def __init__(self):
        self.queue = []
    def is_empty(self):
        return self.queue==[]
    def enqueue(self,item):
        return self.queue.append(item)
    def dequeue(self):
        return self.queue.pop(-1)
    def size(self):
        return len(self.queue)

class queue_likeC:
    """
    original queue class.
    """
    def __init__(self, size):
        self.head = 0
        self.tail = 0
        self.size = size
        self.data = [0]*self.size
    def is_empty(self):
        return self.head == self.tail
    def is_full(self):
        return self.head == (self.tail + 1) % self.size
    def enqueue(self,item):
        if self.is_full():
            return print("overflow.queue.")
        self.data[self.tail] = item
        if self.tail + 1 == self.size:
            self.tail = 0
        else:
            self.tail += 1
    def dequeue(self):
        if self.is_empty():
            return print("underflow.queue.")

        item = self.data[self.head]            
        if self.head + 1 == self.size:
            self.head = 0
        else:
            self.head += 1
        return item
        



    