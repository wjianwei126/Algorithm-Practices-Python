# 和 island count 一样， 不过要输出the labels of the island.
# i.e., given a point (x,y) you need to be able to 说出是哪个岛
class Islands:
    def __init__(self, matrix):
        if not matrix or not matrix[0]:
            raise ValueError('Invalid input')
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.matrix = matrix
        self.labels = []
        for i in range(self.m):
            for j in range(self.n):
                if matrix[i][j] == '1':
                    self.island = set()
                    self.dfs(i, j)
                    self.labels.append(self.island)
        print self.labels

    def dfs(self, i, j):
        if i < 0 or i >= self.m or j < 0 or j >= self.n or self.matrix[i][j] == '0' or self.matrix[i][j] == 'x':
            return
        self.island.add((i, j))
        self.matrix[i][j] = 'x'
        self.dfs(i+1, j)
        self.dfs(i-1, j)
        self.dfs(i, j+1)
        self.dfs(i, j-1)

matrix = [['1', '1', '0'], ['1', '0', '1'], ['0', '1', '1']]
islands = Islands(matrix)
