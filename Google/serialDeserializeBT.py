# Serialize and deserialize a binary tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def serialize(self, node):
        # use pre-order tranversal
        res = []
        stack = [node]
        while stack :
            cur = stack.pop()
            res.append(cur.val)
            if cur.val == '#':
                continue
            if cur.right:
                stack.append(cur.right)
            else:
                stack.append(TreeNode('#'))
            if cur.left:
                stack.append(cur.left)
            else:
                stack.append(TreeNode('#'))
        return res

    def deserialize(self, serial):
        root = TreeNode(serial.pop(0))
        stack = [root]
        while serial:
            node = TreeNode(serial.pop(0))
            leftFlag = True
            if node.val == '#' and leftFlag:
                stack[-1].left = node
                stack.append(node)
            elif node.val == '#' and not leftFlag:
                stack[-1].right = node
                stack.append(node)
                leftFlag = True
            else:
                if leftFlag:
                    leftFlag = False
                else:
                    stack.pop()
                    while stack and stack[-1].right:
                        stack.pop()
        return root

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
print solu.serialize(A)
print solu.deserialize(solu.serialize(A)).val
