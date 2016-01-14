class Node:
    def __init__(self, size):
        self.val = []
        self.maxSize = size
        self.next = None

# class SuperNode:
#     def __init__(self, ma):
#         self.head = None
#         self.maxSize = 10
#         self.size = 0
#         self.next = None

class LinkedListOfArrays:
    def __init__(self, head):
        self.head = head

    def insert(self, value, index):
        fkhead = Node(0)
        fkhead.next = self.head
        node = fkhead
        count = 0
        while node.next and count < index:
            node = node.next
            count += 1

        if count < index:
            node.next = Node(10)
            node.next.val.append(value)
            return

        if len(node.val) < node.maxSize:
            node.val.append(value)
        else:
            temp = node.next
            node.next = Node(10)
            node.next.val.append(value)
            node.next.next = temp
