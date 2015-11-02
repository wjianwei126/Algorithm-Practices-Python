class Coordinates:
    def __init__(self, x, y):
        self.a = x
        self.b = y

class Solution:
    def findPath(self, matrix):
        if not matrix or not matrix[0]: return []
        m = len(matrix)
        n = len(matrix[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        formerSteps = []

        # Here I should create object for each entry
        # Codes like [Coordinates(None, None)] * m creates m references of the same object
        for p in range(m):
            line = []
            for k in range(n):
                line.append(Coordinates(None, None))
            formerSteps.append(line)

        find = False

        queue = [(0, 0, (None, None))]

        while queue:
            x, y, formerCoordinates = queue.pop(0)
            formerSteps[x][y].a = formerCoordinates[0]
            formerSteps[x][y].b = formerCoordinates[1]

            if x == m - 1 and y == n - 1:
                find = True
                break

            matrix[x][y] = -1

            for k in range(4):
                newX = x + directions[k][0]
                newY = y + directions[k][1]

                if newX < 0 or newX >= m or newY < 0 or newY >= n or \
                    matrix[newX][newY] == 1 or matrix[newX][newY] == -1:
                    continue

                queue.append((newX, newY, (x, y)))

        if not find:
            return []
        else:
            res = []
            i, j = m - 1, n - 1
            while i != None and j != None:
                res.insert(0, (i, j))
                temp = formerSteps[i][j]
                i, j = temp.a, temp.b
            return res

solution = Solution()
# No obstacle
matrix = [[0,0,0], [0,0,0], [0,0,0]]
# Output [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2)]

# With obstacles
matrix = [[0,0,0], [1,1,0], [0,0,0], [0,1,1], [0,0,0]]
# Output [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 1), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2)]

# No way out
matrix = [[0,0,0], [1,1,1], [0,0,0]]
# Output []

# More than one path, should output the shortest one
matrix = [[0,0,0,1,1,1], [1,1,0,0,0,0], [0,0,0,1,1,0], [0,1,1,1,0,0], [0,1,1,1,0,1], [0,0,0,0,0,0]]
# Output [(0, 0), (0, 1), (0, 2), (1, 2), (1, 3), (1, 4), (1, 5), (2, 5), (3, 5), (3, 4), (4, 4), (5, 4), (5, 5)]
print solution.findPath(matrix)
