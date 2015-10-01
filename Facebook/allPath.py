# return all the path of a binary tree from root to each leaf
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
	def allPath(self, root):
	    if not root: return ""
	    return self.outputPath(root)
	    
	def outputPath(self, node):
	    if not node: return []
	    re = []
	    if node.left or node.right:
	        leftpath = self.outputPath(node.left)
	        rightpath = self.outputPath(node.right)
	    else:
	        return [node.val]
	    for paths in leftpath:
	        re.append(node.val + paths)
	    for paths in rightpath:
	        re.append(node.val + paths)
	    return re

	def iterativePaths(self, root):
		if not root: return ""
		re = []
		queue = [root]
		pathQ = [root.val]
		while queue:
			node = queue.pop(0)
			tmpRe = pathQ.pop(0)
			if node.left or node.right:
				if node.left:
					queue.append(node.left)
					pathQ.append(tmpRe + node.left.val)
				if node.right:
					queue.append(node.right)
					pathQ.append(tmpRe + node.right.val)
			else:
				re.append(tmpRe)
		return re


	    
if __name__ == "__main__":
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
    solu = Solution()
    print solu.allPath(A)
    print solu.iterativePaths(A)