# // Today, we’re going to be helping Joe. Joe works in a maze.
# // Unfortunately, portions of the maze have caught on fire, and
# // Joe doesn’t have the maze escape manual in his back pocket.
# //
# // Poor Joe! But you can help Joe escape the maze.
# //
# // Given Joe’s location in the maze and which squares of the maze are
# // on fire, you must determine whether Joe can exit the maze before
# // the fire reaches him, and how long it takes to do it (in minutes).
# //
# // Joe and the fire each move one square per minute, vertically or
# // horizontally (not diagonally). The fire spreads in four directions
# // from each square that is on fire. Joe may exit the maze from any
# // square that borders the edge of the maze. Neither Joe nor the fire
# // may enter a square that is occupied by a wall.
# //
# // As an example, consider the maze below:
# //
# // #############   Legend: J = Joe, * = fire, # = wall, |_ = exit
# // # J         #   It will take Joe 14 minutes to exit this maze.
# // ####  ##### #   The fire will be right behind him.
# // |  #  #   # #
# // |  #* #   # #
# // |__#______#_|
# //
# // The maze is represented by the data structure below. I’ve written
# // it in Java, but you can use whatever language you’re most
# // proficient in to solve the problem.
#
# public enum Square { Open, Wall, Fire, Joe };
# public class Maze {
#     Square[][] cells;
# };
#
# public static int escapeTheMaze(Maze maze);

class Maze:
    def __init__(self, cells):
        self.cells = cells
        self.fireMap = [cells]

    def escapeTheMaze(self):
        m = len(self.cells)
        n = len(self.cells[0])

        for i in range(m):
            for j in range(n):
                if self.cells[i][j] == 'J':
                    jX, jY = i, j
                    break

        visited = set()
        queue = [(jX, jY, 0)]

        while queue:
            x, y, curMin = queue.pop(0)

            curMap = self.fireMap[curMin]

            if x < 0 or x >= m or y < 0 or y >= n or curMap[x][y] == '#' \
                or curMap[x][y] == '*' or (x, y) in visited:
                continue

            visited.add((x, y))
            if curMap[x][y] in '|_':
                return curMin + 1

            if curMin + 1 >= len(self.fireMap):
                self.fireMap.append(self.constructNewMap(curMin))

            queue.append((x+1, y, curMin + 1))
            queue.append((x-1, y, curMin + 1))
            queue.append((x, y+1, curMin + 1))
            queue.append((x, y-1, curMin + 1))

        return -1

    def constructNewMap(self, curMin):
        oldMap = self.fireMap[curMin]
        m = len(oldMap)
        n = len(oldMap[0])
        newMap = [[' '] * n for x in range(m)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i in range(m):
            for j in range(n):
                if oldMap[i][j] == ' ':
                    continue
                newMap[i][j] = oldMap[i][j]
                if oldMap[i][j] == '*':
                    for k in directions:
                        if oldMap[i+k[0]][j+k[1]] == ' ':
                            newMap[i+k[0]][j+k[1]] = '*'
        return newMap

cells = ['#############', \
         '# J         #', \
         '####  ##### #', \
         '|  #  #   # #', \
         '|  #* #   # #', \
         '|__#______#_|']
cells = ['######', \
         '#J #*|', \
         '#  # |', \
         '######']
myMaze = Maze(cells)
