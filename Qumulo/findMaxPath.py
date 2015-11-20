class GraphNode:
    def __init__(self, value, surface):
        self.value = value
        self.surface = surface
        self.neighbors = []

class Solution:
    def findMaxPath(self, nodes):
        self.maxVal = float('-inf')
        for node in nodes:
            if node.surface:
                visited = set()
                brokenEdge = set()
                self.dfs(node, visited, brokenEdge, 0, True)
        return self.maxVal

    def dfs(self, node, visited, brokenEdge, curVal, startNode):
        if not startNode and node.surface:
            self.maxVal = max(self.maxVal, curVal + node.value)
            return

        if node not in visited:
            newVal = curVal + node.value
        else:
            newVal = curVal

        visited.add(node)

        for nb in node.neighbors:
            if (node, nb) or (nb, node) in brokenEdge:
                continue
            brokenEdge.add((node, nb))
            self.dfs(nb, visited, brokenEdge, newVal, False)
            brokenEdge.remove((node, nb))
