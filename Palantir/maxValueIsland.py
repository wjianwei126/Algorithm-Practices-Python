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
                    while queue:
                        x, y = queue.pop(0)
                        if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] == 0 or (x, y) in visited:
                            continue
                        visited.add((x, y))
                        curVal += matrix[x][y]
                        queue.append((x+1, y))
                        queue.append((x-1, y))
                        queue.append((x, y+1))
                        queue.append((x, y-1))
                    curMax = max(curMax, curVal)
        return curMax

    def findMaxValueWithNegative(self, matrix):
        if not matrix or not matrix[0]: return None
        m = len(matrix)
        n = len(matrix[0])
        curMax = float('-inf')
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0:
                    queue = [(i, j, 0)]
                    curVal = 0
                    visited = set()
                    localMax = float('-inf')
                    while queue:
                        x, y, nega = queue.pop(0)
                        if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] == 0 or (x, y) in visited:
                            continue
                            
                        visited.add((x, y))

                        if matrix[x][y] < 0:
                            nega += matrix[x][y]
                        else:
                            if nega == 0:
                                curVal += matrix[x][y]
                                localMax = max(localMax, curVal)
                            else:
                                if curVal + nega + matrix[x][y] >= localMax:
                                    curVal += nega + matrix[x][y]
                                    localMax = curVal
                                    nega = 0
                                else:
                                    nega += matrix[x][y]

                        queue.append((x+1, y, nega))
                        queue.append((x-1, y, nega))
                        queue.append((x, y+1, nega))
                        queue.append((x, y-1, nega))

                    curMax = max(curMax, localMax)

        return curMax


solution = Solution()
matrix = [[1,2,0,0], \
          [3,0,4,0], \
          [0,1,0,1]]
matrix = [[1,2,3], \
          [0,-5,0], \
          [0,1,2]]
matrix = [[1,2,3], \
          [0,-1,0], \
          [0,1,2]]
print solution.findMaxValueWithNegative(matrix)
