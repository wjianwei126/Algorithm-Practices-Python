class Matrix:
    def __init__(self, matrix):
        # O(mn)
        self.values = matrix

    def set(self, x, y, n):
        # O(1)
        self.values[x][y] = n

    def query(self, x1, y1, x2, y2):
        # O(mn)
        if x2 < x1 or y2 < y1: return 0
        sum = 0
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                sum += self.values[i][j]
        return sum

class Matrix2:
    def __init__(self, matrix1):
        # O(mn)
        self.values = [[0] * len(matrix1[0]) for x in range(len(matrix))]
        for i in range(len(matrix1)):
            for j in range(len(matrix1[0])):
                self.values[i][j] = matrix1[i][j]
        self.sums = matrix1

        for i in range(1, len(matrix1)):
            self.sums[i][0] = self.sums[i-1][0] + matrix1[i][0]
        for j in range(1, len(matrix1[0])):
            self.sums[0][j] = self.sums[0][j-1] + matrix1[0][j]

        for i in range(1, len(matrix1)):
            for j in range(1, len(matrix1[0])):
                self.sums[i][j] = self.sums[i-1][j] + self.sums[i][j-1] - self.sums[i-1][j-1] + matrix1[i][j]

    def set(self, x, y, n):
        # O(mn)
        diff = n - self.values[x][y]
        for i in range(x, len(self.values)):
            for j in range(y, len(self.values)):
                self.sums[i][j] += diff

    def query(self, x1, y1, x2, y2):
        # O(1)
        if x2 < x1 or y2 < y1: return 0
        if x1 == 0 and x2 == 0:
            return self.sums[x2][y2]
        elif x1 == 0:
            return self.sums[x2][y2] - self.sums[x2][y1-1]
        elif y1 == 0:
            return self.sums[x2][y2] - self.sums[x1-1][y2]
        else:
            return self.sums[x2][y2] - self.sums[x1-1][y2] - self.sums[x2][y1-1] + self.sums[x1-1][y1-1]

matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
m1 = Matrix(matrix)
m2 = Matrix2(matrix1)
print m1.query(1,1,2,2)
print m2.query(1,1,2,2)
m1.set(1,1,10)
m2.set(1,1,10)
print m1.query(1,1,2,2)
print m2.query(1,1,2,2)
