class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mirrorTree(self, root):
        if not root: return None
        newRoot = TreeNode(root.val)
        newRoot.left = self.mirrorTree(root.right)
        newRoot.right = self.mirrorTree(root.left)
        return newRoot

    def mirrorTreeIterative(self, root):
        if not root: return None
        newRoot = TreeNode(root.val)
        queue1 = [root]
        queue2 = [newRoot]
        while queue1:
            old = queue1.pop(0)
            new = queue2.pop(0)
            if old.left:
                newRight = TreeNode(old.left.val)
                new.right = newRight
                queue1.append(old.left)
                queue2.append(new.right)
            if old.right:
                newLeft = TreeNode(old.right.val)
                new.left = newLeft
                queue1.append(old.right)
                queue2.append(new.left)
        return newRoot


solution = Solution()
A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
A.left = B
A.right = C
C.left = D

root = solution.mirrorTreeIterative(A)
print root.val
print root.left.val
print root.right.val
print root.left.right.val
