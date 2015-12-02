class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def linkLeafNode(root):
    if not root: return None
    stack = [root]
    pre = None
    while stack:
        node = stack.pop()
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
        if not node.left and not node.right:
            if pre:
                pre.right = node
                node.left = pre
            pre = node
    return root 
