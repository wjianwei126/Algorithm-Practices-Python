class Solution:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        if not board or len(board) == 0: return
        n = len(board)
        m = len(board[0])
        if n <= 2 or m <= 2: return

        for i in (0, n-1):
            for j in range(m):
                if board[i][j] == 'O':
                    queue = [(i, j)]
                    while queue:
                        x, y = queue.pop(0)
                        if x < 0 or x >= n or y < 0 or y >= m or board[x][y] == 'X' or board[x][y] == 'B':
                            continue
                        board[x][y] = 'B'
                        queue.append((x-1, y))
                        queue.append((x, y-1))
                        queue.append((x+1, y))
                        queue.append((x, y+1))

        for j in (0, m-1):
            for i in range(n):
                if board[i][j] == 'O':
                    queue = [(i, j)]
                    while queue:
                        x, y = queue.pop(0)
                        if x < 0 or x >= n or y < 0 or y >= m or board[x][y] == 'X' or board[x][y] == 'B':
                            continue
                        board[x][y] = 'B'
                        queue.append((x-1, y))
                        queue.append((x, y-1))
                        queue.append((x+1, y))
                        queue.append((x, y+1))

        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'B':
                    board[i][j] = 'O'

if __name__ == "__main__":
    solu = Solution()
    matrix = ['OOO', 'OOO', 'OOO']
    board = [['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']]
    solu.solve(board)
    print matrix
