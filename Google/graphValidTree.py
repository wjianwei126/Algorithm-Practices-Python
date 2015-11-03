class UnionFind:
    def __init__(self, n):
        self.count = n
        self.parent = {}
        for i in range(n):
            self.parent[i] = i

    def find(self, x):
        parent = self.parent[i]
        while parent != self.parent[parent]:
            parent = self.parent[parent]

        return parent

    def union(self, x, y):
        parentX = self.parent[x]
        parentY = self.parent[y]
        if parentX != parentY:
            self.count -= 1
            self.parent[parentX] = parentY
            return True
        else:
            return False

class Solution:
    def graphValidTree(self, n, nodePairs):
        if not nodePairs: return False
        uf = UnionFind(n)
        for pair in nodePairs:
            if not uf.union(pair[0], pair[1]):
                return False
        return uf.count == 1

solution = Solution()
n = 5
nodePairs = [[0, 1], [0, 2], [0, 3], [1, 4]]
nodePairs = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
print solution.graphValidTree(n, nodePairs)
