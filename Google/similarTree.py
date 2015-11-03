# 判断两个二叉树是否相似. tree a is similar to tree b if b can be obtained by 
# switching any nof its odes' left child with its right child
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def similarTree(self, root1, root2):
        if not root1 or not root2: return False
        if root1.val != root2.val: return False
        # if root1.left and root1.right and root2.left and root2.right:
        #     if root1.left.val == root2.left.val and root1.right.val == root2.right.val:
        #         leftJudge =  self.similarTree(root1.left, root2.left)
        #         rightJudge = self.similarTree(root1.right, root2.right)
        #         if leftJudge and rightJudge or not leftJudge and not rightJudge:
        #             return False
        #         else:
        #             return True
        #     elif root1.left.val == root2.right.val and root1.right.val == root2.left.val:
        #         return self.sameTree(root1.left, root2.right) and self.sameTree(root1.right, root2.left)
        #     else:
        #         return False
        # elif root1.left and not root1.right and root2.right and not root2.left:
        #     return self.sameTree(root1.left, root2.right)
        # elif root1.right and not root1.left and root2.left and not root2.right:
        #     return self.sameTree(root1.right, root2.left)
        # else:
        #     return False
        if not root1.left and not root1.right and not root2.left and not root2.right:
            return False

        if self.sameTree(root1.left, root2.right) and self.sameTree(root1.right, root2.left):
            return True
        elif self.sameTree(root1.left, root2.left) and self.similarTree(root1.right, root2.right):
            return True
        elif self.sameTree(root1.right, root2.right) and self.similarTree(root1.left, root2.left):
            return True
        else:
            return False


    def sameTree(self, root1, root2):
        if not root1 and not root2: return True
        if root1 and root2:
            if root1.val != root2.val:
                return False
            else:
                return self.sameTree(root1.left, root2.left) and self.sameTree(root1.right, root2.right)
        else:
            return False

nodes = [TreeNode(i) for i in range(6)]
nodes[0].left = nodes[1]
nodes[0].right = nodes[2]
nodes[1].left = nodes[3]
nodes[1].right = nodes[4]
nodes[2].left = nodes[5]

nodes1 = [TreeNode(i) for i in range(6)]
nodes1[0].left = nodes1[1]
nodes1[0].right = nodes1[2]
nodes1[1].left = nodes1[4]
nodes1[1].right = nodes1[3]
nodes1[2].left = nodes1[5]

solution = Solution()
print solution.similarTree(nodes[0], nodes1[0])
