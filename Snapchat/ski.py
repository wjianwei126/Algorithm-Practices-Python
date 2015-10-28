class Solution:
    def ski(self, mountain):
        if not mountain or not mountain[0]: return 0
        res = 0
        self.m = len(mountain)
        self.n = len(mountain[0])
        self.dp = [[0] * self.n for x in range(self.m)]
        self.mountain = mountain
        for i in range(self.m):
            for j in range(self.n):
                temp = self.dfs(i, j)
                res = max(res, temp)
        return res

    def dfs(self, i, j):
        if self.dp[i][j] != 0:
            return self.dp[i][j]
        #res = 1
        self.dp[i][j] = 1
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for k in range(4):
            x = i + direction[k][0]
            y = j + direction[k][1]

            if x < 0 or x >= self.m or y < 0 or y >= self.n:
                continue
            if self.mountain[x][y] < self.mountain[i][j]:
                temp = 1 + self.dfs(x, y)
                self.dp[i][j] = max(self.dp[i][j], temp)

        return self.dp[i][j]

solu = Solution()
mountain = [[6,9,8,7], [5,10,8,6], [4,3,4,5], [1,2,3,1]]
print solu.ski(mountain)
