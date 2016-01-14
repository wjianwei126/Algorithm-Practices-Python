class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class SuperNode:
    def __init__(self, ma):
        self.head = None
        self.maxSize = 10
        self.size = 0
        self.next = None
