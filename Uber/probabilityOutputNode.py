import random
class Node:
    def __init__(self, id, weight):
        self.id = id
        self.weight = weight
        self.next = None

class Solution:
    def probabilityOutputNode(self, head):
        # O(n) time O(1) space
        if not head: return
        node = head
        totalWeight = 0
        while node:
            totalWeight += node.weight
            node = node.next
        r = random.randint(1, totalWeight)
        node = head
        accumWeight = 0
        while node:
            accumWeight += node.weight
            if accumWeight >= r:
                return node.id
            node = node.next

    def probabilityOutputNodeMap(self, head):
        if not head: return
        dic = {}
        idMap = {}
        start = i = 0
        totalWeight = 0
        node = head
        while node:
            idMap[i] = node.id
            totalWeight += node.weight
            dic[i] = (start, start+node.weight)
            start += node.weight
            node = node.next
            i += 1

        #O(logn)
        r = random.randint(1, totalWeight)
        left = 0
        right = i - 1
        while left <= right:
            mid = left + (right - left) / 2
            if dic[mid][0] < r and dic[mid][1] >= r:
                return idMap[mid]
            elif r <= dic[mid][0]:
                right = mid - 1
            else:
                left = mid + 1


solution = Solution()
A = Node(2, 2)
B = Node(3, 5)
C = Node(1, 3)
A.next = B
B.next = C
dic = {1:0, 2:0, 3:0}
for i in range(10000):
    label = solution.probabilityOutputNodeMap(A)
    dic[label] += 1
print dic
