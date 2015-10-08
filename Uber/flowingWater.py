class Solution:
    def search(self, i, j, visited):
        stack = [(i, j)]
        while stack:
            x, y = stack.pop()
            if x < 0 or x >= self.m or y < 0 or y >= self.n or self.mat[x][y] in visited:
                continue
            visited.add((x, y))
            direc = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for k in range(4):
                newX = x + direc[k][0]
                newY = y + direc[k][1]
                if self.mat[newX][newY] in '~*':
                    continue
                if self.mat[newX][newY] >= self.mat[x][y] and (newX, newY) not in visited:
                    stack.append((newX, newY))

    def flowingWater(self, mat):
        self.m = len(mat)
        self.n = len(mat[0])
        self.mat = mat

        visited_pac = set()
        for i in range(1, self.m-1):
            self.search(i, 1, visited_pac)
        for j in range(1, self.n-1):
            self.search(1, j, visited_pac)

        visited_atl = set()
        for i in range(1, self.m-1):
            self.search(i, self.n-2, visited_atl)
        for j in range(1, self.n-1):
            self.search(self.m-2, j, visited_atl)

        return visited_pac & visited_atl


solution = Solution()
mountain = ['~~~~~~~', '~12235*', '~32344*', '~24531*', '~67145*', '~51124*', '*******']
# mountain = ['~~~~', '~25*', '~86*', '****']
print solution.flowingWater(mountain)
