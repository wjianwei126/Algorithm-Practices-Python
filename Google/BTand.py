class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def BTand(self, root1, root2):
        if not root1 and not root2: return None
        return self.helper(root1, root2)

    def helper(self, root1, root2):
        if root1.val == '*' and root2.val == '*':
            root = TreeNode('*')
            leftNode = self.helper(root1.left, root2.left)
            rightNode = self.helper(root1.right, root2.right)
            root.left = leftNode
            root.right = rightNode
        elif root1.val == 0 or root2.val == 0:
            root = TreeNode(0)
        elif root1.val == 1:
            root = self.deepCopy(root2)
        elif root2.val == 1:
            root = self.deepCopy(root1)
        return root

    def deepCopy(self, root):
        if not root: return None
        newRoot = TreeNode(root.val)
        leftNode = self.deepCopy(root.left)
        rightNode = self.deepCopy(root.right)
        newRoot.left = leftNode
        newRoot.right = rightNode
        return newRoot

A = TreeNode('*')
B = TreeNode(1)
C = TreeNode('*')
D = TreeNode(0)
E = TreeNode(1)
A.left = B
A.right = C
C.left = D
C.right = E

a = TreeNode('*')
b = TreeNode('*')
c = TreeNode(0)
d = TreeNode(1)
e = TreeNode(0)
a.left = b
a.right = c
b.left = d
b.right = e

solution = Solution()
root = solution.BTand(A, a)

stack = []
node = root
while stack or node:
    if node:
        stack.append(node)
        node = node.left
    else:
        node = stack.pop()
        print node.val
        node = node.right
