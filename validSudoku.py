class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        return self.isValidRow(board) and self.isValidCol(board) and self.isValidSqr(board)
    def isValidRow(self, board):
        for row in board:
            if not self.isValidUnit(row):
                return False
        return True
    def isValidCol(self, board):
        for i in range(len(board[0])):
            col = []
            for j in range(len(board)):
                col.append(board[j][i])
            if not self.isValidUnit(col):
                return False
        return True
    def isValidSqr(self, board):
        for i in (0,3,6):
            for j in (0,3,6):
                temp = []
                for p in range(i, i+3):
                    for q in range(j, j+3):
                        temp.append(board[p][q])
                if not self.isValidUnit(temp):
                    return False
        return True
    def isValidUnit(self, units):
        dic = {}
        for num in units:
            if num != '.':
                if num in dic:
                    return False
                else:
                    dic[num] = 1
        return True

if __name__ == "__main__":
    solu = Solution()
    board = [".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]
    print solu.isValidSudoku(board)
