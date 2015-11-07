# Serialize and deserialize a binary tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    res = []

    def serialize(self, root):
        if not root:
            self.res.append('#')
            return
        self.res.append(root.val)
        self.serialize(root.left)
        self.serialize(root.right)

    def deserialize(self, data):
        if not data or data[0] == '#':
            data.pop(0)
            return None
        root = TreeNode(data[0])
        data.pop(0)
        root.left = self.deserialize(data)
        root.right = self.deserialize(data)
        return root

    def checkValid(self, nodes):
        if not nodes: return True
        stack = []
        i = 0
        while i < len(nodes):
            print stack
            while len(stack) > 2 and stack[-1] == '#' and stack[-2] == '#':
                stack.pop()
                stack.pop()
                stack.pop()
                stack.append('#')
            stack.append(nodes[i])
            i += 1
        while len(stack) > 2 and stack[-1] == '#' and stack[-2] == '#':
            stack.pop()
            stack.pop()
            stack.pop()
            stack.append('#')
        return stack == ['#']

solu = Solution()
A = TreeNode('A')
B = TreeNode('B')
C = TreeNode('C')
D = TreeNode('D')
E = TreeNode('E')
F = TreeNode('F')
G = TreeNode('G')
A.left = B
B.left = C
A.right = D
D.left = E
D.right = F
F.left = G
solu.serialize(A)
# print solu.res
# root = solu.deserialize(solu.res)
# stack = []
# node = root
# while stack or node:
#     if node:
#         print node.val
#         if node.right:
#             stack.append(node.right)
#         node = node.left
#     else:
#         node = stack.pop()

print solu.checkValid([9, 3, 4, '#', '#', 1, 2, '#', '#', '#'])

class NAryTree:
    def __init__(self, x):
        self.val = x
        self.children = []

class Solution2:
    res = []
    def serialize(self, root):
        if not root:
            return
        self.res.append(root.val)
        for child in root.children:
            self.serialize(child)
        self.res.append('#')

    def deserialize(self, data):
        if not data or data[0] == '#':
            data.pop(0)
            return True, None
        root = NAryTree(data[0])
        data.pop(0)
        while True:
            end, node = self.deserialize(data)
            if end:
                break
            root.children.append(node)
        return False, root

    def traverse(self, root):
        if root:
            print root.val
            for child in root.children:
                self.traverse(child)
A = NAryTree('A')
B = NAryTree('B')
C = NAryTree('C')
D = NAryTree('D')
E = NAryTree('E')
F = NAryTree('F')
G = NAryTree('G')
H = NAryTree('H')
I = NAryTree('I')
J = NAryTree('J')
K = NAryTree('K')
A.children = [B,C,D]
B.children = [E, F]
F.children = [K]
D.children = [G,H,I,J]
solu = Solution2()
solu.serialize(A)
# print solu.res
# end, root = solu.deserialize(solu.res)
# solu.traverse(root)
