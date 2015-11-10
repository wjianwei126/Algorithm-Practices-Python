import random
class MineDetector:
    def __init__(self, m, n, k):
        self.board = [[0] * n for x in range(m)]
        self.m = m
        self.n = n
        self.k = k

    def genBoard(self):
        mines = random.sample(range(self.m*self.n), self.k)
        for index in mines:
            x = index / self.n
            y = index % self.n
            self.board[x][y] = '*'
        surrounding = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for i in range(self.m):
            for j in range(self.n):
                if self.board[i][j] == '*':
                    continue
                for k in surrounding:
                    newX = i + k[0]
                    newY = j + k[1]
                    if newX >= 0 and newX < self.m and newY >= 0 and newY < self.n and self.board[newX][newY] == '*':
                        self.board[i][j] += 1
        return self.board

md = MineDetector(5, 5, 20)
print md.genBoard()
