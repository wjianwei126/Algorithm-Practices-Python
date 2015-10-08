class Solution(object):
    def swapNode(self, head):
        if not head or not head.next: return head
        fkhead = ListNode(0)
        fkhead.next = head
        cur = fkhead
        while cur.next and cur.next.next:
            tmp = cur.next.next.next
            cur.next.next.next = cur.next
            cur.next = cur.next.next
            cur.next.next.next = tmp
            cur = cur.next.next

        return fkhead.next



solution = Solution()
A = None
A = ListNode(1)
B = ListNode(2)
A.next = B
C = ListNode(3)
B.next = C

node = A
while node:
    print node.val, '->',
    node = node.next
print ''

node = solution.swapNode(A)
while node:
    print node.val, '->',
    node = node.next
