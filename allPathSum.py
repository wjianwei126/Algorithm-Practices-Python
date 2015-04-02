# Output all the path sums of a tree, from the root to each of the leaves.
# e.g.       1
#           / \
#          2   5
#         / \
#        3   4
# output = 6+7+6 = 19

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution_recursive:
	def allPathSum(self, root):
		return self.pathSum(root, 0)

	def pathSum(self, node, prev):
		if not node: return 0
		sum = prev + node.val
		if ((not node.left) and (not node.right)):
			return sum

		return self.pathSum(node.left, sum) + self.pathSum(node.right, sum)

class Solution_iteritive:
	def allPathSum(self, root):
		queue = [root]
		sumqueue = [root.val]
		cursum = 0
		while queue:
			node = queue.pop(0)
			if node.left or node.right:
				prevsum = sumqueue.pop(0)
				if node.left:
					queue.append(node.left)
					sumqueue.append(prevsum + node.left.val)
				if node.right:
					queue.append(node.right)
					sumqueue.append(prevsum + node.right.val)
			else:
				cursum += sumqueue.pop(0)

		return cursum

