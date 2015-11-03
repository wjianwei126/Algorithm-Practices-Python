class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def linkedListGroups(self, head, nodes):
        if not nodes or not head: return 0
        nodeSet = set(nodes)
        node = head
        count = 0
        while nodeSet and node:
            if node in nodeSet:
                count += 1
                while nodeSet and node in nodeSet:
                    nodeSet.remove(node)
                    node = node.next
            else:
                node = node.next
        return count

solution = Solution()
A = ListNode('a')
B = ListNode('b')
C = ListNode('c')
D = ListNode('d')
E = ListNode('e')
F = ListNode('f')
G = ListNode('g')
H = ListNode('h')
A.next = B
B.next = C
C.next = D
D.next = E
E.next = F
F.next = G
G.next = H
nodes = [C, D, F, B, H]
print solution.linkedListGroups(A, nodes)
