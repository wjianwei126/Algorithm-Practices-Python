# Serialize and deserialize a binary tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root: return ''
        queue = [root]
        res = []
        while queue:
            node = queue.pop(0)
            if not node:
                res.append('#')
                continue
            res.append(str(node.val))
            nextLeft = node.left if node.left else None
            nextRight = node.right if node.right else None
            queue += [nextLeft, nextRight]
        return ','.join(res)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        data = data.split(',')
        root = TreeNode(data.pop(0))
        queue = [root]
        left = True
        while data:
            nxt = data.pop(0)
            node = TreeNode(nxt) if nxt != '#' else None
            if node:
                queue.append(node)
            if left:
                queue[0].left = node
            else:
                queue[0].right = node
                queue.pop(0)
            left = not left
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
print solu.deserialize(solu.serialize(A)).left.val
