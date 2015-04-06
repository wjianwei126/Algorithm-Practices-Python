# convert a binary tree to double linked list
class TreeNode:
	def __init__ (self, x):
		self.val = x
		self.left = None
		self.right = None
class Solution:
	def converter(self, root):
		if not root: return None
		if root.left:
			left = root.left
			self.converter(left)
			while left.right:
				left = left.right
			left.right = root
			root.left = left
		if root.right:
			right = root.right
			self.converter(right)
			while right.left:
				right = right.left
			root.right = right
			right.left = root
		while root.left:
			root = root.left
		return root

if __name__ == "__main__":
	solu = Solution()
	A = TreeNode("a")
	B = TreeNode("b")
	C = TreeNode("c")
	D = TreeNode("d")
	E = TreeNode("e")
	F = TreeNode("f")
	G = TreeNode("g")
	H = TreeNode("h")
	A.left = B
	A.right = E
	B.left = C
	B.right = D
	E.left = F
	F.left = G
	F.right = H
	root = solu.converter(A)
	while root:
		print root.val
		if root.right:
			root = root.right
		else:
			break
	while root:
		print root.val
		if root.left:
			root = root.left
		else:
			break



