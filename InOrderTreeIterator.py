# Iterator for in-order traversal of binary tree.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self, root):
        self.stack = []
        self.pushall(root)
        self.cur = self.stack.pop()
    
    def value(self):
        return self.cur.val
        
    def next(self):
        self.pushall(self.cur.right)
        self.cur = self.stack.pop()
        
    def hasNext(self):
        return not (len(self.stack) == 0 and not self.cur.right) 
        
    def pushall(self, node):
        while node:
            self.stack.append(node)
            node = node.left

class inorderTraversal:
    def inorderTraversal(self, node):
        stack = []
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                print node.val
                node = node.right
        
	
if __name__ == "__main__":
    A = TreeNode("a")
    B = TreeNode("b")
    C = TreeNode("c")
    D = TreeNode("d")
    E = TreeNode("e")
    F = TreeNode("f")
    G = TreeNode("g")
    H = TreeNode("h")
    
    A.left = B
    A.right = E
    B.left = C
    B.right = D
    E.left = F
    F.left = G
    F.right = H
    
    solu = Solution(A)
    solu2 = inorderTraversal()
    solu2.inorderTraversal(A)
    print "  "
    while 1:
        print solu.value()
        if solu.hasNext():
            solu.next()
        else:
            break