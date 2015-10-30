class Node:
    def __init__(self, x):
        self.val = x
        self.color = None
        self.neighbors = set()

class Graph:
    def __init__(self):
        self.nodes = set()

    def addEdge(self, a, b):
        a.neighbors.add(b)
        b.neighbors.add(a)
        self.nodes.add(a)
        self.nodes.add(b)

    def isBipartite(self):
        if not self.nodes: return False
        for node in self.nodes:
            if not node.color:
                queue = [(node, 1)]
                while queue:
                    cur, color = queue.pop(0)
                    cur.color = color
                    for neighbor in cur.neighbors:
                        if not neighbor.color:
                            queue.append((neighbor, 1 - color))
                        elif neighbor.color == color:
                            return False
        return True

graph = Graph()
A = Node('a')
B = Node('b')
C = Node('c')
D = Node('d')
E = Node('e')
graph.addEdge(A, B)
graph.addEdge(A, C)
# graph.addEdge(B, C)
graph.addEdge(D, E)
graph.addEdge(B, E)
graph.addEdge(A, E)
print graph.isBipartite()
