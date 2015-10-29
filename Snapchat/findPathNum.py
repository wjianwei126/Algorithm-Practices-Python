class Solution:
    def findPathNum(self, startX, startY, endX, endY, k):
        if abs(startX - endX) + abs(startY - endY) > k:
            return 0
        res = 0
        queue = [(startX, startY, k)]
        while queue:
            x, y, remain = queue.pop(0)
            if remain == 0:
                if x == endX and y == endY:
                    res += 1
                continue
            direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for i in range(4):
                newX = x + direction[i][0]
                newY = y + direction[i][1]
                if newX < 0 or newX >= 8 or newY < 0 or newY >= 8:
                    continue
                queue.append((newX, newY, remain - 1))
        return res


solution = Solution()
print solution.findPathNum(0, 0, 2, 2, 6)
