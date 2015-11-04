class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, node):
        if not root:
            self.root = node
        else:
            if root.val < node.val:
                if not root.right:
                    root.right = node
                else:
                    self.insert(root.right, node)
            else:
                if not root.left:
                    root.left = node
                else:
                    self.insert(root.left, node)

    def search(self, target):
        node = self.root
        while node:
            if node.val == key:
                return node
            elif node.val > key:
                node = node.left
            else:
                node = node.right

        return -1

    def delete(self, key):
        self.root = self.deleteHelper(root, key)

    def deleteHelper(self, root, key):
        if not root: return None

        if key < root.val:
            root.left = self.deleteHelper(root.left, key)
        elif key > root.val:
            root.right = self.deleteHelper(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            root.val = self.minValue(root.right)
            root.right = self.deleteHelper(root.right, root.val)

        return root

    def minValue(self, node):
        while node.left:
            node = node.left
        return node

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print root.val
            self.inorder(root.right)
