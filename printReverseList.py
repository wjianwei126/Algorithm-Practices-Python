# Question: print reverse list
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def printReverse(self, node):
        if not node: return 
        self.printReverse(node.next)
        print node.val
    
    def iterativePrint(self, node):
        if not node: return 
        stack = []
        while stack or node:
            if node:
                stack.append(node)
                node = node.next
            else:
                print stack.pop().val
        
if __name__ == "__main__":
    A = ListNode("a")
    B = ListNode("b")
    C = ListNode("c")
    D = ListNode("d")
    
    A.next = B
    B.next = C
    C.next = D

    solu = Solution()
    solu.printReverse(A)
    solu.iterativePrint(A)