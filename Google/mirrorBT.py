# Write a function that takes in abinary tree and returns a mirror of the binary tree.
#      1
#   2     3
# 4   5
# Mirror should be
#
#      1
#   3     2
#       5   4
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mirrorBT(self, root):
        if not root: return None
        left = self.mirrorBT(root.right)
        right = self.mirrorBT(root.left)
        root.left = left
        root.right = right
        return root

    def mirrorBTIterative(self, root):
        if not root: return None
        leftQ = [root.left]
        rightQ = [root.right]
        rootQ = [root]
        while leftQ:
            node = rootQ.pop(0)
            left = leftQ.pop(0)
            right = rightQ.pop(0)
            node.left = right
            node.right = left
            if left:
                leftQ.append(left.left)
                rightQ.append(left.right)
                rootQ.append(left)
            if right:
                leftQ.append(right.left)
                rightQ.append(right.right)
                rootQ.append(right)
        return root

    def levelOrderTraversal(self, root):
        if not root: return []
        curLine = [root]
        res = [[root.val]]
        nextLine = []
        temp = []
        while curLine:
            node = curLine.pop(0)
            if node.left:
                nextLine.append(node.left)
                temp.append(node.left.val)
            if node.right:
                nextLine.append(node.right)
                temp.append(node.right.val)
            if not curLine:
                curLine = nextLine
                if len(temp) > 0:
                    res.append(temp)
                    temp = []
                nextLine = []
        return res

nodes = [TreeNode(i) for i in range(6)]
nodes[0].left = nodes[1]
nodes[0].right = nodes[2]
nodes[1].left = nodes[3]
nodes[1].right = nodes[4]
nodes[2].left = nodes[5]

solution = Solution()
print solution.levelOrderTraversal(nodes[0])
newRoot = solution.mirrorBT(nodes[0])
# print newRoot.val, newRoot.left.val, newRoot.right.val
print solution.levelOrderTraversal(newRoot)
root = solution.mirrorBTIterative(newRoot)
print solution.levelOrderTraversal(root)
