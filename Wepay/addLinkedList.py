class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseLinkedList(head):
    if not head: return None
    fkhead = ListNode(0)
    fkhead.next = head
    while head.next:
        tmp = head.next.next
        head.next.next = fkhead.next
        fkhead.next = head.next
        head.next = tmp
    return fkhead.next

def addList(head1, head2):
    newHead1 = reverseLinkedList(head1)
    newHead2 = reverseLinkedList(head2)

    p1 = newHead1
    p2 = newHead2
    carry = 0
    fkhead = ListNode(0)
    node = fkhead
    while p1 or p2:
        num1 = 0 if not p1 else p1.val
        num2 = 0 if not p2 else p2.val
        digitSum = num1 + num2 + carry
        node.next = ListNode(digitSum % 10)
        carry = digitSum / 10
        node = node.next
        if p1: p1 = p1.next
        if p2: p2 = p2.next
    if carry > 0:
        node.next = ListNode(carry)
    return reverseLinkedList(fkhead.next)

l1 = ListNode(4)
l2 = ListNode(2)
l1.next = l2
r1 = ListNode(1)
r2 = ListNode(7)
r3 = ListNode(2)
r1.next = r2
r2.next = r3

head = addList(l1, r1)
while head:
    print head.val
    head = head.next
