# You have a sorted binary tree and you want to select the ith smallest
# element from the tree
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def findithSmallest(root, i):
    # inorder traversal
    stack = []
    res = []
    node = root
    while node or stack:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            res.append(node)
            node = node.right
    return res[i-1]
