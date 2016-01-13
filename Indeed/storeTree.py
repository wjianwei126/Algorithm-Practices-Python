# There are several ways to store a binary tree to make it space efficient
# According to the number of nodes in the tree (full down to sparse)
class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

HEIGHT = 4
# If the tree is almost full
def storeTreeInArray(root):
    if not root: return [None]
    treeList = [None] * (2 ** HEIGHT)
    queue = [(root, 1)]
    while queue:
        node, index = queue.pop(0)
        treeList[index] = node.val
        if node.left:
            queue.append((node.left, index*2))
        if node.right:
            queue.append((node.right, index*2+1))
    return treeList

def recoverFromArray(treeList):
    if len(treeList) < 2: return None
    root = TreeNode(treeList[1])
    queue = [root]
    for i in range(2, len(treeList), 2):
        if treeList[i] != None:
            left = TreeNode(treeList[i])
            queue[0].left = left
            queue.append(left)
        if treeList[i+1] != None:
            right = TreeNode(treeList[i+1])
            queue[0].right = right
            queue.append(right)
        queue.pop(0)
    return root

# If the tree is not that full but also not so sparse
def storeTreeInTwoArrays(root):
    if not root: return [], []
    valueList = []
    indexList = []
    queue = [(root, 1)]
    while queue:
        node, index = queue.pop(0)
        valueList.append(node.val)
        indexList.append(index)
        if node.left:
            queue.append((node.left, index*2))
        if node.right:
            queue.append((node.right, index*2+1))
    return valueList, indexList

def recoverFromTwoArrays(valueList, indexList):
    if not valueList or not indexList: return None
    dic = {}
    dic[1] = TreeNode(valueList[0])
    for i in range(1, len(valueList)):
        parentIndex = indexList[i] / 2
        if indexList % 2 == 0:
            dic[parentIndex].left = TreeNode(valueList[i])
        else:
            dic[parentIndex].right = TreeNode(valueList[i])
    return dic[1]

A = TreeNode('A')
B = TreeNode('B')
C = TreeNode('C')
D = TreeNode('D')
E = TreeNode('E')
F = TreeNode('F')
A.left = B
A.right = C
C.left = D
C.right = E
D.right = F

print storeTreeInArray(A)
print storeTreeInTwoArrays(A)
