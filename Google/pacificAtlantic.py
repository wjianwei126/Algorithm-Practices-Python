class Solution:
    def pacificAtlantic(self, matrix):
        if not matrix or not matrix[0]: return []
        self.map = matrix
        m = len(matrix)
        n = len(matrix[0])
        res = []
        self.visited = set()
        self.dp = [[(-1, -1)] * n for x in range(m)]
        for i in range(m):
            for j in range(n):
                paci, alta = self.dfs(i, j)
                if paci and alta:
                    res.append((i,j))
        print self.dp
        return res

    def dfs(self, x, y):
        if self.dp[x][y][0] != -1 and self.dp[x][y][1] != -1:
            return self.dp[x][y]

        self.visited.add((x, y))

        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        pac = False
        alt = False
        if x == 0 or y == 0:
            pac = True
        if x == len(self.map) - 1 or y == len(self.map[0]) - 1:
            alt = True

        for k in range(4):
            newX = x + direction[k][0]
            newY = y + direction[k][1]

            if newX < 0 or newX >= len(self.map) or newY < 0 or newY >= len(self.map[0]):
                continue

            if self.map[newX][newY] < self.map[x][y] or self.map[newX][newY] == self.map[x][y] and (newX, newY) not in self.visited:
                findPac, findAlta = self.dfs(newX, newY)
                if findPac:
                    pac = True
                if findAlta:
                    alt = True

        self.dp[x][y] = (pac, alt)
        return self.dp[x][y]

solution = Solution()
matrix = [[1,2,3,4,6],[1,2,6,5,7], [6,8,8,5,3], [10,9,8,7,1]]
print solution.pacificAtlantic(matrix)
