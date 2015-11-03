class UnionFind:
    def __init__(self, n):
        self.count = n
        self.parent = {}
        for i in range(n):
            self.parent[i] = i

    def find(self, x):
        parent = self.parent[x]
        while parent != self.parent[parent]:
            parent = self.parent[parent]

        pa = self.parent[x]
        while pa != self.parent[pa]:
            temp = self.parent[pa]
            self.parent[pa] = parent
            pa = temp

        return parent

    def union(self, x, y):
        parentX = self.find(x)
        parentY = self.find(y)
        if parentX != parentY:
            self.count -= 1
            self.parent[parentY] = parentX
            return True
        else:
            return False

    def find2(self, x):
        return self.parent[x]

    def union2(self, x, y):
        parent = self.parent[x]
        if parent == self.parent[y]:
            return False
        self.count -= 1
        for i in self.parent.keys():
            if self.parent[i] == parent:
                self.parent[i] = self.parent[y]
