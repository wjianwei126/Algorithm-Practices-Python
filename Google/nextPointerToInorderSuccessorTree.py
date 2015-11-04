class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    def inorderTraversal(self, root):
        if not root: return []
        res = []
        node = root
        visited = set()
        while node:
            if node.left and node.left not in visited:
                node = node.left
            else:
                res.append(node.val)
                visited.add(node)
                if node.right:
                    node = node.right
                else:
                    node = node.next
        return res

    def inorder(self, root):
        if not root: return []
        stack = []
        res = []
        node = root
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                res.append(node.val)
                node = node.right
        return res

nodes = [TreeNode(i) for i in range(8)]
nodes[0].left = nodes[1]
nodes[0].right = nodes[2]
nodes[1].left = nodes[3]
nodes[3].right = nodes[5]
nodes[2].right = nodes[4]
nodes[5].left = nodes[6]
nodes[5].right = nodes[7]
nodes[1].next = nodes[0]
nodes[6].next = nodes[5]
nodes[7].next = nodes[1]
solution = Solution()
print solution.inorder(nodes[0])
print solution.inorderTraversal(nodes[0])
