class TreeNode:
	def __init__(self, x):
		self.val = x		
		self.left = None
		self.right = None

class Solution:
	def reconstruct(self, lists):
		if not lists: return None
		root = TreeNode(lists.pop(0))
		stack = [root]
		flag = 0
		while lists:
			node = TreeNode(lists.pop(0))
			if node.val != "*" and flag == 0:
				stack[-1].left = node
				stack.append(node)
			elif node.val != "*" and flag == 1:
				stack[-1].right = node
				stack.append(node)
				flag = 0
			else:
				if flag == 0:
					flag = 1
				elif flag == 1:
					stack.pop()
					while stack and stack[-1].right:
						stack.pop()
		return root

	def depth(self, root):
		if not root: return 0
		left_depth = self.depth(root.left)
		right_depth = self.depth(root.right)
		return left_depth + 1 if left_depth >= right_depth  else right_depth + 1

if __name__ == "__main__":
	solu = Solution()
	inputList1 = [1, 2, "*", "*", 3, 4, "*", "*", "*"]
	inputList2 = [1, 2, "*", 3, "*", "*", 4, "*", 5, 6, "*", "*", "*"]
	inputList3 = []
	inputList4 = [1, 2, 3, "*", 4, "*", "*", "*", 5, "*", 6, 7, "*", "*", "*"]
	
	print solu.depth(solu.reconstruct(inputList4)) 
