# a matrix, 0 represents empty, 1 represents obstacl. 
# find whether there's a path between 2 nodes.
class Solution:
	row = 0
	col = 0
	tar_x = 0
	tar_y = 0
	def ifPath(self, matrix, s_x, s_y, e_x, e_y):
		if not matrix or s_x == None or s_y == None or e_x == None or e_y == None:
			return False
		self.row = len(matrix)
		self.col = len(matrix[0])
		self.tar_x = e_x
		self.tar_y = e_y
		return self.dfs(matrix, s_x, s_y)

	def dfs(self, matrix, i, j):
		if i < 0 or i >= self.row or j < 0 or j >= self.col or matrix[i][j] != 0:
			return False
		if i == self.tar_x and j == self.tar_y:
			return True
		matrix[i][j] = "x"
		return self.dfs(matrix, i-1, j) \
				or self.dfs(matrix, i+1, j) \
				or self.dfs(matrix, i, j-1) \
				or self.dfs(matrix, i, j+1)

	def iterativeDFS(self, matrix, s_x, s_y, e_x, e_y):
		if not matrix or s_x == None or s_y == None or e_x == None or e_y == None:
			return False
		self.row = len(matrix)
		self.col = len(matrix[0])
		self.tar_x = e_x
		self.tar_y = e_y
		stack = [(s_x, s_y)]
		while stack:
			cur = stack.pop()
			if cur[0] < 0 or cur[0] >= self.row or cur[1] < 0 or cur[1] >= self.col or matrix[cur[0]][cur[1]] != 0:
				continue
			if cur[0] == self.tar_x and cur[1] == self.tar_y:
				return True
			matrix[cur[0]][cur[1]] = "x"
			stack.append((cur[0]-1, cur[1]))
			stack.append((cur[0]+1, cur[1]))
			stack.append((cur[0], cur[1]-1))
			stack.append((cur[0], cur[1]+1))
		return False

if __name__ == "__main__":
	solu = Solution()
	matrix =[[0,1,0,0,1], [1,1,1,0,0], [1,0,0,0,1], [0,0,0,0,1]]
	#print solu.ifPath(matrix,3,0,0,0)
	print solu.iterativeDFS(matrix,3,0,0,2)
