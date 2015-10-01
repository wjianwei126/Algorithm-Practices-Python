# Reverse a Singly Linked List.
# Example Input: A -> B -> C
# Example Output: C -> B -> A
class ListNode:
	def __init__ (self, x):
		self.val = x
		self.next = None

class Solution:
	head = ListNode(0)

	def iterativeReverse(self, node):
		if not node: return None
		fkhead = ListNode(0)
		fkhead.next = node
		first = one = node
		two = node.next
		while first.next:
			rest = two.next
			fkhead.next = two
			two.next = one
			first.next = rest
			one = two
			two = rest

		return fkhead.next

	def recursive(self, node):
		if not node: return 
		if not node.next:
			self.head = node
			return 
		self.recursive(node.next)
		node.next.next = node
		node.next = None
		return self.head

if __name__ == "__main__":
	A = ListNode("a")
	B = ListNode("b")
	C = ListNode("c")
	D = ListNode("d")

	A.next = B
	B.next = C
	C.next = D
	solu = Solution()
	#head = solu.iterativeReverse(A)
	head = solu.recursive(A)
	while head:
		print head.val
		head = head.next
