# "给一个Vector<vector<int>>表示一个房间，INT_MAX表示墙，INT_MIN表示各种equipment，
# 0表示空位置。现在要放一个fountain，离所有equipment总距离最短。问放在哪里好。
# LZ用的bfs（还不小心写成dfs了被小哥指出尼玛。。我刚要改，写了个queue，
# 小哥说不用了这个改还要花点时间，我就直接注明你要用bfs了。。撞墙）
# follow up：时间复杂度，LZ说是O(mnk)。问有木有更快的，LZ并没直接想出来。
# 小哥说可以bfs过程中做一下greedy（然而我总感觉这样不是optimal解），
# 后来又说可以一开始就把任意两个点间距离算出来。"
class Solution:
    def placeFountain(self, matrix):
        if not matrix or not matrix[0]: return []
        m = len(matrix)
        n = len(matrix[0])
        distanceMap = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):

                if matrix[i][j] == 'w':
                    distanceMap[i][j] = float('inf')

                if matrix[i][j] == 'e':
                    visited = [['x'] * n for _ in range(m)]
                    queue = [(i, j, 0)]
                    while queue:
                        x, y, distance = queue.pop(0)
                        if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] == 'w' or visited[x][y] == 'o':
                            continue
                        visited[x][y] = 'o'
                        distanceMap[x][y] += distance
                        queue.append((x+1, y, distance+1))
                        queue.append((x-1, y, distance+1))
                        queue.append((x, y+1, distance+1))
                        queue.append((x, y-1, distance+1))

        shortest = float('inf')
        res = []
        for i in range(m):
            for j in range(n):
                if distanceMap[i][j] < shortest:
                    res = [(i, j)]
                    shortest = distanceMap[i][j]
                elif distanceMap[i][j] == shortest:
                    res.append((i, j))
        print distanceMap
        return shortest, res

solution = Solution()
matrix = [[], []]
matrix = [[0,0,'w','w'], [0,0,0,0], ['w','w',0,'w'], [0,0,0,'w']]
matrix = [[0,0,'w','w'], [0,'e',0,'e'], ['w','w','e','w'], ['e',0,0,'w']]
matrix = [[0,0,0,0], [0,'e',0,'e'], [0,0,0,0], ['e',0,'e',0]]
print solution.placeFountain(matrix)
