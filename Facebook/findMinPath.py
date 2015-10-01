# find minimum path in the tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findMinPath (self, root):
        if not root: return []
        Min, minlist = self.findMin(root)
        return minlist
    
    def findMin(self, root):
        if not root:
            return (2147483648, [])
        if not root.left and not root.right:
            return (root.val, [root.val])
        leftmin, leftlist = self.findMin(root.left)
        rightmin, rightlist = self.findMin(root.right)
        if leftmin < rightmin:
            curmin = min(root.val, leftmin)
            curlist = leftlist + [root.val]
        else:
            curmin = min(root.val, rightmin)
            curlist = rightlist + [root.val]
        return curmin, curlist

if __name__ == "__main__":
    A = TreeNode(5)
    B = TreeNode(10)
    C = TreeNode(1)
    D = TreeNode(7)
    E = TreeNode(3)
    F = TreeNode(8)
    
    A.left = B
    A.right = E
    B.left = C
    B.right = D
    E.left = F
    
    solu = Solution()
    print solu.findMinPath(A)