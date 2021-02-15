"""
スタックやキュートのデータ構造
"""

class stack:
    """
    python's stack class.
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

    