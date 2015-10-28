# zigzag print一个matrix，input: [ [1, 2, 3], [4, 5, 6] ] output: [ [1], [2, 3], [3, 5], [6] ].
class Solution:
    def zigzagPrint(self, matrix):
        if not matrix: return []
        m = len(matrix)
        n = len(matrix[0])
        res = []
        for j in range(n):
            temp = []
            x, y = 0, j
            while x < m and y >= 0:
                temp.append(matrix[x][y])
                x += 1
                y -= 1
            res.append(temp)
        for i in range(1, m):
            temp = []
            x, y = i, n-1
            while x < m and y >= 0:
                temp.append(matrix[x][y])
                x += 1
                y -= 1
            res.append(temp)
        return res

solution = Solution()
matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
matrix = [[1]]
matrix = []
matrix = [[1,2,3]]
matrix = [[1,2,3], [4,5,6], [7,8,9]]
matrix = [[1,2,3], [4,5,6], [7,8,9], [10,11,12]]
print solution.zigzagPrint(matrix)
