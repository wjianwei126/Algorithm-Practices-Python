# Given points and edges, return whether any two points are connected in the graph
class UnionFind:
    def __init__(self, pointsN):
        self.parent = [i for i in range(pointsN)]

    def find(self, i):
        # O(1)
        return self.parent[i]

    def unite(self, x, y):
        # O(n)
        root = self.parent[x]
        for i in range(len(self.parent)):
            if self.parent[i] == root:
                self.parent[i] = self.parent[y]


    # def find(self, i):
    #     while self.parent[i] != i:
    #         #self.parent[i] = self.parent[self.parent[i]]
    #         i = self.parent[i]
    #     return self.parent[i]
    #
    # def union(self, x, y):
    #     xRoot = self.find(x)
    #     yRoot = self.find(y)
    #     self.parent[xRoot] = yRoot
class Solution:
    def unionFind(self, edges, pointsN):
        if not edges and len(pointsN) > 1: return False
        unionSet = UnionFind(pointsN)
        for i in range(len(edges)):
            unionSet.unite(edges[i][0], edges[i][1])
        root = unionSet.parent[0]
        print unionSet.parent
        for i in range(1, len(unionSet.parent)):
            if unionSet.parent[i] != root:
                return False
        return True


solution = Solution()
edges = [[1,2], [0,4], [2,4]]
pointsN = 5
print solution.unionFind(edges, pointsN)
