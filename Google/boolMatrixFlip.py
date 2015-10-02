# Given a 2D boolean matrix initialized as all false, write a function flip() to randomly flip a false to true.
# This function may be called several times.
import random
class BoolMatrix:
    def __init__(self, matrix):
        # O(mn) time initialization O(mn) space
        self.matrix = matrix
        self.falseList = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == False:
                    self.falseList.append((i,j))

    def flip(self):
        candidate = random.randint(0, len(self.falseList)-1)
        x, y = self.falseList[candidate]
        del self.falseList[candidate] # O(1) or O(mn)?
        self.matrix[x][y] = True

class BoolMatrix2:
    def flip(self, matrix):
        # http://www.1point3acres.com/bbs/thread-142665-3-1.html
        # O(mn) time, O(m) space
        falseList = []
        temp = 0
        # O(mn)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == False:
                    temp += 1
            falseList.append(temp)
        candidate = random.randint(1, falseList[-1])
        # O(m)
        for i in range(len(falseList)):
            if falseList[i] >= candidate:
                x = i
                if i == 0:
                    k = candidate
                else:
                    k = candidate - falseList[i-1]
                break
        # O(n)
        for j in range(len(matrix[0])):
            if matrix[x][j] == False:
                if k > 1:
                    k -= 1
                else:
                    y = j
                    break
        matrix[x][y] = True
        return matrix


matrix = [[False] * 4 for x in range(3)]

# M = BoolMatrix(matrix)
# M.flip()
# print M.matrix
# M.flip()
# print M.matrix
# M.flip()
# print M.matrix
M = BoolMatrix2()
matrix = M.flip(matrix)
print matrix
matrix = M.flip(matrix)
print matrix
matrix = M.flip(matrix)
print matrix
matrix = M.flip(matrix)
print matrix
