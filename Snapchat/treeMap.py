class TreeNode:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.left = None
        self.right = None

class TreeMap:
    def __init__(self):
        self.root = None

    def put(self, key, value):
        if not self.root:
            self.root = TreeNode(key, value)
            return
        node = self.root
        while node:
            if key > node.key:
                if node.right:
                    node = node.right
                else:
                    node.right = TreeNode(key, value)
                    break
            elif key < node.key:
                if node.left:
                    node = node.left
                else:
                    node.left = TreeNode(key, value)
                    break
            else:
                node.val = value
                break

    def get(self, key):
        if not self.root: return -1
        node = self.root
        while node:
            if key > node.key:
                node = node.right
            elif key < node.key:
                node = node.left
            else:
                return node.val
        if not node: return -1

    def delete(self, key):
        self.root = self.deleteHelper(self.root, key)

    def deleteHelper(self, root, key):
        if not root: return None

        if key < root.key:
            root.left = self.deleteHelper(root.left, key)
        elif key > root.key:
            root.right = self.deleteHelper(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                node = self.minKeyNode(root.right)
                root.key, root.val = node.key, node.val
                root.right = self.deleteHelper(root.right, root.key)
        return root

    def minKeyNode(self, node):
        while node.left:
            node = node.left
        return node

    def inOrder(self, root):
        if not root: return
        self.inOrder(root.left)
        print root.key, root.val
        self.inOrder(root.right)

treeMap = TreeMap()
# print treeMap.get(4)
treeMap.put(5, 'a')
treeMap.put(6, 'c')
treeMap.put(4, 'b')
treeMap.put(5.5, 'd')
# print treeMap.get(6)
# print treeMap.get(4)
# print treeMap.get(5.5)
# print treeMap.get(5.7)
# treeMap.put('a', 'dd')
# print treeMap.get('a')
# treeMap.inOrder(treeMap.root)
treeMap.delete(5)
treeMap.inOrder(treeMap.root)
