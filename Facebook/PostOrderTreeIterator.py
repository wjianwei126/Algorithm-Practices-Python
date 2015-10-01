# tree iterator post-order
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
class Solution:
    def __init__(self, root):
        self.stack = []
        self.cur = root
        self.preVisit = None
        while self.cur.left:
            self.stack.append(self.cur)
            self.cur = self.cur.left
    
    def curValue(self):
        return self.cur.val
        
    def hasNext(self):
        return self.cur and self.stack
        
    def next(self):
        self.preVisit = self.cur
        peeknode = self.stack[-1]
        if peeknode.right and peeknode.right != self.preVisit:
            
            self.cur = peeknode.right
            while self.cur.left:
                self.stack.append(self.cur)
                self.cur = self.cur.left
            
        else:
            self.cur = self.stack.pop()
            
        

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
    A.right = C
    B.left = D
    B.right = E
    E.left = G
    E.right = H
    C.left = F
    
    solu = Solution(A)
    
    while True:
        print solu.curValue()
        if solu.hasNext():
            solu.next()
        else:
            break