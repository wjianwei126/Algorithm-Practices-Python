#给一个0 1 矩阵，连在一起的1算做岛。求问岛的个数
#11001
#10011
#这就是2个岛

class Solution:
	row = 0
	col = 0
	def islandCounting(self, matrix):
		if not matrix: return 0
		self.row = len(matrix)
		self.col = len(matrix[0])
		count = 0
		for i in range(self.row):
			for j in range(self.col):
				if matrix[i][j] == 1:
					count += 1
					self.dfs(matrix, i, j)
		return count

	def dfs(self, matrix, i, j):
		if i < 0 or i >= self.row or j < 0 or j >= self.col or matrix[i][j] != 1:
			return 
		matrix[i][j] = 'x'
		self.dfs(matrix, i-1, j)
		self.dfs(matrix, i+1, j)
		self.dfs(matrix, i, j-1)
		self.dfs(matrix, i, j+1)

	def iterativeCounting(self, matrix):
		if not matrix: return 0
		self.row = len(matrix)
		self.col = len(matrix[0])
		count = 0
		for i in range(self.row):
			for j in range(self.col):
				if matrix[i][j] == 1:
					count += 1
					stack = [(i,j)]
					while stack:
						cur = stack.pop()
						if cur[0] < 0 or cur[0] >= self.row or cur[1] < 0 or cur[1] >= self.col or matrix[cur[0]][cur[1]] != 1:
							continue
						matrix[cur[0]][cur[1]] = 'x'
						stack.append((cur[0]-1, cur[1]))
						stack.append((cur[0]+1, cur[1]))
						stack.append((cur[0], cur[1]-1))
						stack.append((cur[0], cur[1]+1))
		return count

if __name__ == "__main__":
	solu = Solution()
	matrix = [[1,1,0,0,1], [1,0,0,1,1]]
	#print solu.islandCounting(matrix)
	print solu.iterativeCounting(matrix)
	print matrix
