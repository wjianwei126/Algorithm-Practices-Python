class TreeNode:
    def __init__(self):
        self.color = None
        self.children = []

def getIntersection(root1, root2):
    if not root1: return root2
    if not root2: return root1
    return bfs(root1, root2)

def bfs(node1, node2):
    node = TreeNode()
    if node1.color == 'w':
        node = node2
    elif node2.color == 'w':
        node = node1
    elif node1.color == 'b' and node2.color == 'b':
        node = node1
    elif not node1.color and not node2.color:
        for k in range(4):
            node.children.append(bfs(node1.children[k], node2.children[k]))
    else:
        node.color = 'b'
    return node
