class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def converter(self, root):
        if not root: return None
        if root.left:
            leftNode = self.converter(root.left)
            while leftNode.right:
                leftNode = leftNode.right
            leftNode.right = root
            root.left = leftNode
        if root.right:
            rightNode = self.converter(root.right)
            rightNode.left = root
            root.right = rightNode
        while root.left:
            root = root.left
        return root

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
while root.right:
	print root.val
	root = root.right
print root.val
