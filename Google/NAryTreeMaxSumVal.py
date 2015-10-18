class NAryTree:
    def __init__(self, x):
        self.val = x
        self.children = []

class Solution:
    def NAryTreeMaxSumVal(self, root):
        if not root: return 0
        self.map = {}
        return self.helper(root, -1)

    def helper(self, node, parentVal):
        if not node: return 0
        if node in self.map and parentVal in self.map[node]:
            return self.map[node][parentVal]

        subTreeMax = 0
        bestVal = 0
        for i in range(1, 11):
            if i == parentVal: continue
            tempSum = i
            for child in node.children:
                tempSum += self.helper(child, i)
            if tempSum > subTreeMax:
                subTreeMax = tempSum
                bestVal = i

        node.val = bestVal
        if node not in self.map:
            self.map[node] = {}
        self.map[node][parentVal] = subTreeMax
        return subTreeMax

A = NAryTree(0)
B = NAryTree(0)
C = NAryTree(0)
D = NAryTree(0)
E = NAryTree(0)
F = NAryTree(0)
G = NAryTree(0)
H = NAryTree(0)
I = NAryTree(0)
J = NAryTree(0)
A.children = [B]
B.children = [C, D, E]
E.children = [F, G, H, I, J]
solution = Solution()
print solution.NAryTreeMaxSumVal(A)
