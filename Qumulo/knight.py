def findPath(matrix, m, n, x1, y1, x2, y2):
    if not matrix or not matrix[0]: return 0
    queue = [(x1, y1, 0)]
    res = float('inf')
    while queue:
        x, y, step = queue.pop(0)
        if x == x2 and y == y2:
            res = min(res, step)
            continue
        if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] == '*':
            continue
        matrix[x][y] = '*'
        direction = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2)]
        for i in range(8):
            newX = x + direction[i][0]
            newY = y + direction[i][1]
            queue.append((newX, newY, step + 1))
    return res
m, n = map(int, raw_input().split(' '))
x1, y1 = map(int, raw_input().split(' '))
x2, y2 = map(int, raw_input().split(' '))
matrix = [['O'] * n for _ in xrange(m)]
blockNum = int(raw_input())
for i in xrange(blockNum):
    x, y = map(int, raw_input().split(' '))
    matrix[x][y] = '*'
print findPath(matrix, m, n, x1, y1, x2, y2)
