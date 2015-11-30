class Solution:
    def findMaxValue(self, matrix):
        if not matrix or not matrix[0]: return None
        m = len(matrix)
        n = len(matrix[0])
        curMax = float('-inf')
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0:
                    queue = [(i, j)]
                    curVal = 0
                    visited = set()
                    localMax = float('-inf')
                    while queue:
                        x, y = queue.pop(0)
                        if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] == 0 or (x, y) in visited:
                            continue
                        visited.add((x, y))
                        curVal += matrix[x][y]
                        # print x, y, curVal, localMax
                        # direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                        # for k in range(4):
                        #     newX, newY = x + direction[k][0], y + direction[k][1]
                        #     if newX < 0 or newX >= m or newY < 0 or newY >= n or matrix[newX][newY] == 0 or (newX, newY) in visited:
                        #         continue
                        #     queue.append((newX, newY, curVal + matrix[newX][newY]))
                        queue.append((x+1, y))
                        queue.append((x-1, y))
                        queue.append((x, y+1))
                        queue.append((x, y-1))
                    # print i, j, localMax
                    curMax = max(curMax, curVal)
        return curMax

solution = Solution()
matrix = [[1,2,0,0], \
          [3,0,4,0], \
          [0,1,0,1]]
# matrix = [[1,2,3], \
#           [0,-5,0], \
#           [0,1,2]]
# matrix = [[1,2,3], \
#           [0,-1,0], \
#           [0,1,2]]
print solution.findMaxValue(matrix)
