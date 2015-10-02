# Longest consecutive numbers in a binary tree
# http://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=143234&extra=page%3D1%26filter%3Dsortid%26sortid%3D311%26searchoption%5B3046%5D%5Bvalue%5D%3D1%26searchoption%5B3046%5D%5Btype%5D%3Dradio%26sortid%3D311
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def longestConsecutiveNumsinBT(self, root):
        if not root: return []
        stack = [(root, [root.val])]
        res = []
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                res.append(path)
                continue
            if node.left:
                if node.left.val == node.val + 1:
                    stack.append((node.left, path + [node.left.val]))
                else:
                    stack.append((node.left, [node.left.val]))
            if node.right:
                if node.right.val == node.val + 1:
                    stack.append((node.right, path + [node.right.val]))
                else:
                    stack.append((node.right, [node.right.val]))

        longest = res[0]
        for i in range(1, len(res)):
            if len(res[i]) > len(longest):
                longest = res[i]
        return longest


solu = Solution()
A = TreeNode(1)
B = TreeNode(4)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)
F = TreeNode(5)
G = TreeNode(6)
# H = TreeNode(4)
A.right = C
C.left = B
C.right = D
D.right = E
B.right = F
F.left = G

print solu.longestConsecutiveNumsinBT(A)
