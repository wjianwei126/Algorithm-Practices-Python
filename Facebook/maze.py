# w stands for wall, g stands for gate, find the distance for each "_" to the nearest gate
# input:      output:
# _ W G _     3 W G 1
# _ _ _ W     2 2 1 W
# _ W _ W     1 W 2 W
# G W _ _     G W 3 4

class Solution:
	def findDis(self, maze):
		if not maze or len(maze) == 0 or len(maze[0]) == 0: return
		m = len(maze)
		n = len(maze[0])
		for i in range(m):
			for j in range(n):
				if maze[i][j] == "G":
					queue = [(i+1,j,1), (i-1,j,1), (i,j-1,1), (i,j+1,1)]
					while queue:
						a, b, count = queue.pop(0)
						if a < 0 or a >= m or b < 0 or b >= n or maze[a][b] in ["G", "W"]:
							continue

						if maze[a][b] == "_":
							maze[a][b] = count
						elif maze[a][b] > count:
							maze[a][b] = count
						else:
							continue

						queue.append((a+1, b, count+1))
						queue.append((a-1, b, count+1))
						queue.append((a, b-1, count+1))
						queue.append((a, b+1, count+1))

		return maze

if __name__ == "__main__":
	solu = Solution()
	maze = [["_", "W", "G", "_"], ["_", "_", "_", "W"], ["_", "W", "_", "W"], ["G", "W", "_", "_"]]
	print solu.findDis(maze)

