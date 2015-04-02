#all "1" in a matrix that stands next to each other represents an island. Find the size of each island.
#0 1 0 0 1
#1 1 1 0 0
#1 0 0 0 1
#0 0 0 0 1                   output 5 1 2

class Solution:
	row = 0
	col = 0
	def islandSize(self, matrix):
		if not matrix: return 0
		self.row = len(matrix)
		self.col = len(matrix[0])
		re = []
		for i in range(self.row):
			for j in range(self.col):
				if matrix[i][j] == 1:
					re.append(self.dfs(matrix, i, j))

		return re

	def dfs(self, matrix, i, j):
		if i < 0 or i >= self.row or j < 0 or j >= self.col or matrix[i][j] != 1:
			return 0
		matrix[i][j] = 'x'
		return 1 + self.dfs(matrix, i-1, j) + self.dfs(matrix, i+1, j) + self.dfs(matrix, i, j-1) +  self.dfs(matrix, i, j+1)

	def iterativeDFS(self, matrix):
		if not matrix: return 0
		self.row = len(matrix)
		self.col = len(matrix[0])
		re = []
		for i in range(self.row):
			for j in range(self.col):
				if matrix[i][j] == 1:
					stack = [(i, j)]
					count = 0
					while stack:
						cur = stack.pop()
						if cur[0] < 0 or cur[0] >= self.row or cur[1] < 0 or cur[1] >= self.col or matrix[cur[0]][cur[1]] != 1:
							continue
						count += 1
						matrix[cur[0]][cur[1]] = "x"
						stack.append((cur[0]-1, cur[1]))
						stack.append((cur[0]+1, cur[1]))
						stack.append((cur[0], cur[1]-1))
						stack.append((cur[0], cur[1]+1))
					re.append(count)
		return re

	def bfs(self, matrix):
		if not matrix: return 0
		self.row = len(matrix)
		self.col = len(matrix[0])
		re = []
		for i in range(self.row):
			for j in range(self.col):
				if matrix[i][j] == 1:
					queue = [(i,j)]
					count = 0
					while queue:
						cur = queue.pop(0)
						if cur[0] < 0 or cur[0] >= self.row or cur[1] < 0 or cur[1] >= self.col or matrix[cur[0]][cur[1]] != 1:
							continue
						count += 1
						matrix[cur[0]][cur[1]] = "x"
						queue.append((cur[0]-1, cur[1]))
						queue.append((cur[0]+1, cur[1]))
						queue.append((cur[0], cur[1]-1))
						queue.append((cur[0], cur[1]+1))
					re.append(count)

		return re


if __name__ == "__main__":
	solu = Solution()
	matrix =[[0,1,0,0,1], [1,1,1,0,0], [1,0,0,0,1], [0,0,0,0,1]]
	#print solu.islandSize(matrix)
	#print solu.iterativeDFS(matrix)
	print solu.bfs(matrix)