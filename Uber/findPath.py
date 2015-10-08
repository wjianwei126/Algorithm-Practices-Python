class Solution(object):
    def findPath(self, matrix, x1, y1, x2, y2):
        if not matrix or not matrix[0]: return False
        m = len(matrix)
        n = len(matrix[0])
        queue = [(x1, y1, [(x1, y1)])]
        while queue:
            x, y, path = queue.pop(0)
            if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] == -1:
                continue
            if x == x2 and y == y2:
                return True, path
            queue.append((x-1, y, path+[(x-1, y)]))
            queue.append((x+1, y, path+[(x+1, y)]))
            queue.append((x, y-1, path+[(x, y-1)]))
            queue.append((x, y+1, path+[(x, y+1)]))
        return False

solution = Solution()
matrix =  [[0,0,0,-1,0],[0,-1,0,'B',0],[0,-1,-1,-1,0],[0,'A',-1,0,0],[0,0,-1,0,0],[0,0,0,0,0]]
print solution.findPath(matrix, 3, 1, 1, 3)
