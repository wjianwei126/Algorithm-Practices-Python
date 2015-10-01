# Return a node in BST whose value is the closest to a target
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def closestNode(self, root, target):
        if not root: return None
        prev = None
        node = root
        while node:
            if node.val == target:
                return node
            elif node.val > target:
                if not prev:
                    res = node
                else:
                    if abs(res.val - target) > abs(node.val - target):
                        res = node
                prev = node
                node = node.left
            else:
                if not prev:
                    res = node
                else:
                    if abs(res.val - target) > abs(node.val - target):
                        res = node
                prev = node
                node = node.right
        return res

A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5.5)
F = TreeNode(7)
G = TreeNode(10)
H = TreeNode(8)

D.left = B
D.right = F
B.left = A
B.right = C
F.left = E
F.right = G
G.left = H
solu = Solution()
target = 12
print solu.closestNode(D, target).val
