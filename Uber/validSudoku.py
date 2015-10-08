class Solution(object):
    def isValidSudoku(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: bool
        """
        if not matrix or not matrix[0]: return False
        if not self.isValidRow(matrix):
            return False
        if not self.isValidCol(matrix):
            return False
        if not self.isValidBox(matrix):
            return False
        return True

    def isValidRow(self, matrix):
        for row in matrix:
            if not self.isValidUnit(row):
                return False
        return True

    def isValidCol(self, matrix):
        for i in range(len(matrix[0])):
            col = []
            for j in range(len(matrix)):
                col.append(matrix[j][i])
            if not self.isValidUnit(col):
                return False
        return True

    def isValidBox(self, matrix):
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                box = []
                for x in range(3):
                    for y in range(3):
                        box.append(matrix[i+x][j+y])
                if not self.isValidUnit(box):
                    return False
        return True

    def isValidUnit(self, nums):
        numSet = set()
        for n in nums:
            if n == '.':
                continue
            if n not in numSet:
                numSet.add(n)
            else:
                return False
        return True
