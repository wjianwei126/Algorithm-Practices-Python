# 一个2d array of char, 'X'表示不能走, " "表示草地, 给一个初始x,y 
# 然后把所有的草除掉并回到原点. 要求的是,每走一步打印一个方向, 最后打印出所有的方向...
# 想到了是dfs, 但是卡在往回走的过程了... 最后没写出全部的代码, 还被大叔嘲讽了..
# 其实并不太难, dfs 可以解决. 主要是题目略长,然后时间比较不够了, 这种题套模板会比较快.
class Solution:
    def printPath(self, board, x, y):
        buf = [(x,y)]
        visited = set(buf)
        result = []
        dir = [(-1,0), (1,0), (0,-1), (0,1)]
        while buf:
            cur = buf[-1]
            flag = False
            for d in dir:
                n_x, n_y = cur[0]+d[0], cur[1]+d[1]
                if self.isValid(board, n_x, n_y) and not (n_x, n_y) in visited:
                    result.append(d)
                    buf.append((n_x, n_y))
                    visited.add((n_x, n_y))
                    flag = True
                    break
            if not flag:
                cur = buf.pop()
                if buf:
                    result.append((buf[-1][0]-cur[0], buf[-1][1]-cur[1]))

        return result

    def isValid(self, board, x, y):
        if x<0 or x>=len(board) or y<0 or y>=len(board[0]):
            return False
        if board[x][y]=='x':
            return False
        return True


sol = Solution()
result = sol.printPath(["x  x", "xx  ", "x   ", "    "], 0, 1)
print result
