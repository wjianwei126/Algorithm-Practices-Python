# Given two binary trees A and B. Figure out if A is the sonTree of B
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sonTree(self, A, B):
        if not A : return True
        if A and not B: return False
        stack = [B]
        while stack:
            node = stack.pop()
            if node.val == A.val:
                if self.isSameTree(A, node):
                    return True
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False

    def isSameTree(self, n1, n2):
        if not n1 and n2: return False
        if not n2 and n1: return False
        if not n1 and not n2: return True
        if n1.val != n2.val: return False
        return self.isSameTree(n1.left, n2.left) and self.isSameTree(n1.right, n2.right)

A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(4)
D = TreeNode(0)
E = TreeNode(1)
F = TreeNode(2)
G = TreeNode(3)
H = TreeNode(4)

A.left = B
A.right = C
D.left = E
D.right = H
E.left = F
E.right = G

solu = Solution()
print solu.sonTree(A, D)
