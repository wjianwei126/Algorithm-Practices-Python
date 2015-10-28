class GraphNode:
    def __init__(self, x):
        self.val = x
        self.neighbors = []

class Solution:
    def hasCycle(self, node):
        if not node: return False
        self.visited = set()
        self.finished = set()
        self.cycle = False
        self.dfs(node)
        return self.cycle

    def dfs(self, node):
        self.visited.add(node)
        print node.val
        for neighbor in node.neighbors:
            if neighbor in self.finished:
                continue
            if neighbor in self.visited:
                self.cycle = True
                continue
            self.dfs(neighbor)
        self.finished.add(node)

A = GraphNode('a')
B = GraphNode('b')
C = GraphNode('c')
D = GraphNode('d')
E = GraphNode('e')
A.neighbors = [B, C]
B.neighbors = [E]
C.neighbors = [B]
D.neighbors = [B]
E.neighbors = [D]
solution = Solution()
print solution.hasCycle(A)
