class Solution:
    def numberOfIsland(self, matrix):
        if not matrix or not matrix[0]: return 0
        count = 0
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    count += 1
                    stack = [(i, j)]
                    while stack:
                        x, y = stack.pop()
                        if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] != 1:
                            continue
                        matrix[x][y] = 'x'
                        stack.append((x-1, y))
                        stack.append((x+1, y))
                        stack.append((x, y-1))
                        stack.append((x, y+1))

        return count

solu = Solution()
matrix = [[1,1,0,0,1], [1,0,0,1,1]]
print solu.numberOfIsland(matrix)
