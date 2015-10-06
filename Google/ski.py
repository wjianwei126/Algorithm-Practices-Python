class Solution:
    def ski(self, mountain):
        if not mountain or not mountain[0]: return 0
        self.mountain = mountain
        m = len(mountain)
        n = len(mountain[0])
        self.dp = [[0] * n for x in range(m)]

        res = 0
        for i in range(m):
            for j in range(n):
                tmp = self.dfs(i, j)
                res = max(res, tmp)
        return res

    def dfs(self, i, j):
        if self.dp[i][j] != 0:
            return self.dp[i][j]

        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        self.dp[i][j] = 1
        for k in range(4):
            x = i + direction[k][0]
            y = j + direction[k][1]

            if x < 0 or x >= len(self.mountain) or y < 0 or y >= len(self.mountain[0]):
                continue

            if self.mountain[i][j] > self.mountain[x][y]:
                tmp = self.dfs(x, y) + 1
                self.dp[i][j] = max(tmp, self.dp[i][j])

        return self.dp[i][j]

    def skiIterative(self, mountain):
        if not mountain or not mountain[0]: return 0
        m = len(mountain)
        n = len(mountain[0])
        dp = [[0] * n for x in range(m)]
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        res = 0
        for i in range(m):
            for j in range(n):
                stack = [(i, j, 0)]
                length = 1
                while stack:
                    x, y, path = stack.pop()
                    if dp[x][y] != 0:
                        length = max(length, path + dp[x][y])
                        continue

                    end = True
                    for k in range(4):
                        _x = x + direction[k][0]
                        _y = y + direction[k][1]

                        if _x < 0 or _x >= m or _y < 0 or _y >= n:
                            continue

                        if mountain[x][y] > mountain[_x][_y]:
                            end = False
                            stack.append((_x, _y, path+1))
                    if end:
                        dp[x][y] = 1
                        length = max(length, path + 1)
                dp[i][j] = length
                res = max(res, dp[i][j])
        print dp
        return res


solu = Solution()
mountain = [[6,9,8,7], [5,10,8,6], [4,3,4,5], [1,2,3,1]]
print solu.ski(mountain)
print solu.skiIterative(mountain)
