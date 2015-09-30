class LRUCache1(object):
    # use OrderedDict
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dic = collections.OrderedDict()
        self.remain = capacity

    def get(self, key):
        """
        :rtype: int
        """
        if key not in self.dic:
            return -1
        else:
            value = self.dic.pop(key)
            self.dic[key] = value
            return value

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.dic:
            self.dic.pop(key)
        else:
            if self.remain > 0:
                self.remain -= 1
            else:
                self.dic.popitem(last=False)
        self.dic[key] = value

class LRUCache2(object):
    # use dictionary and two-end queue
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dic = {}
        self.queue = []
        self.remain = capacity

    def get(self, key):
        """
        :rtype: int
        """
        if key not in self.dic:
            return -1
        else:
            self.queue.remove(key)
            self.queue.append(key)
            return self.dic[key]

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.dic:
            self.queue.remove(key)
            self.queue.append(key)
        else:
            if self.remain > 0:
                self.remain -= 1
            else:
                lruKey = self.queue[0]
                del self.dic[lruKey]
                self.queue.pop(0)
            self.queue.append(key)
        self.dic[key] = value

class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache3(object):
    # use double linked list and dictionary
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dic = {}
        self.remain = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        """
        :rtype: int
        """
        if key not in self.dic:
            return -1
        cur = self.dic[key]
        cur.prev.next = cur.next
        cur.next.prev = cur.prev

        self.moveToTail(cur)

        return self.dic[key].value

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.dic:
            self.dic[key].value = value
            node = self.dic[key]
            node.prev.next = node.next
            node.next.prev = node.prev
        else:
            if self.remain > 0:
                self.remain -= 1
            else:
                del self.dic[self.head.next.key]
                self.head.next = self.head.next.next
                self.head.next.prev = self.head
            node = Node(key, value)
            self.dic[key] = node
        self.moveToTail(node)

    def moveToTail(self, node):
        node.prev = self.tail.prev
        self.tail.prev = node
        node.prev.next = node
        node.next = self.tail
