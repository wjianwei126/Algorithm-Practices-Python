class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []
        self.weight = []

def rootToLeafMinCost(root):
    if not root: return None
    stack = [(root, [root.val], 0)]
    minCost = float('inf')
    minPath = None
    while stack:
        node, path, cost = stack.pop()
        if not node.children:
            if cost < minCost:
                minPath = path
                minCost = cost
            continue
        for i in range(len(node.children)):
            stack.append((node.children[i], path + node.children[i].val, cost + node.weight[i]))

    return minPath, minCost
    
class Solution:
    def rootToLeafMinCostRecursive(root):
        if not root: return None
        self.minCost = float('inf')
        self.minPath = None
        dfs(root, [root.val], 0)
        return self.minPath, self.minCost

    def dfs(node, path, cost):
        if not node.children:
            if cost < self.minCost:
                self.minPath = path
                self.minCost = cost
            return
        for i in range(len(node.children)):
            dfs(node.children[i], path + node.children[i].val, cost + node.weight[i])
