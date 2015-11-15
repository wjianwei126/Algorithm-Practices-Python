class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size):
        self.size = size
        self.array = [None] * self.size

    def put(self, key, value):
        index = hash(key) % self.size
        if not self.array[index]:
            self.array[index] = ListNode(key, value)
        else:
            node = self.array[index]
            while node:
                if node.key == key:
                    node.value = value
                    return
                if not node.next:
                    node.next = ListNode(key, value)
                    return
                node = node.next

    def get(self, key):
        index = hash(key) % self.size
        if not self.array[index]:
            return None
        node = self.array[index]
        while node:
            if node.key == key:
                return node.value
            node = node.next
        return None

hashtable = HashTable(100)
print hashtable.get(542)
hashtable.put(542, 'asdfa')
print hashtable.get(542)
hashtable.put('abc', 234)
print hashtable.get('abc')
hashtable.put(542, 'aaaaa')
print hashtable.get(542)
