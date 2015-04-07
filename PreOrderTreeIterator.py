# tree iterator pre-order
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
class Solution:
    def __init__(self, root):
        self.stack = []
        if root.right:
            self.stack.append(root.right)
        self.cur = root
    
    def curValue(self):
        return self.cur.val
        
    def hasNext(self):
        return self.cur and (self.cur.left or self.cur.right or self.stack)
        
    def next(self):
        if self.cur.left:
            self.cur = self.cur.left
        else:
            self.cur = self.stack.pop()
        if self.cur.right:
            self.stack.append(self.cur.right)

if __name__ == "__main__":
    
    A = TreeNode("a")
    B = TreeNode("b")
    C = TreeNode("c")
    D = TreeNode("d")
    E = TreeNode("e")
    F = TreeNode("f")
    A.left = B
    A.right = C
    B.left = D
    B.right = E
    C.left = F
    
    solu = Solution(A)
    
    while True:
        print solu.curValue()
        if solu.hasNext():
            solu.next()
        else:
            break