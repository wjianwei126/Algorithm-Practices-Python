# Given a sequencialized preorder traversal list of a binary tree, output its height.
# e.g. {1, 2, *, *, 3, 4, *, *, *} stands for 
#     1
#    / \
#   2   3
#      /
#     4
#

class TreeNode:
	def __init__(self, x):
		self.val = x		
		self.left = None
		self.right = None

class Solution1:
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

class Solution2:
	def findDepth(self, enc):
		lists = enc.split(" ")
		#print lists
		index = 0
		if not lists: 
			return 0
		return self.depth(lists, index)
	def depth(self, lists, index):
		#print self.index
		if lists[index] == "*": return 0
		index += 1
		#print self.index
		left_depth = self.depth(lists, index)

		index += 1
		#print self.index

		right_depth = self.depth(lists, index)
		#print left_depth, right_depth
		return left_depth + 1 if left_depth >= right_depth else right_depth + 1


if __name__ == "__main__":
	solu = Solution2()
	inputList1 = "1 * *"   #depth 3
	inputList2 = "1 2 * * *"    #depth 4
	inputList3 = "ab * *"	  #depth 0
	inputList4 = [1, 2, 3, "*", 4, "*", "*", "*", 5, "*", 6, 7, "*", "*", "*"]   #depth 4
	
	print solu.findDepth(inputList1) 
	print solu.findDepth(inputList2) 
	print solu.findDepth(inputList3) 

