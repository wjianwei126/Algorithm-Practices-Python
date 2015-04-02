#flood fill。
#题目是有一个矩阵, 1代表已经染色，0代表没有染色。
#完成一个函数，
#输入：矩阵a，整数x， 整数y
#输出: 
#返回一个矩阵，为以(x,y)点（0-based）为开始点的染色结果，将其周围区域染色，直到遇到已经染色的位置或边界为止。
#若(x, y)已经染色则直接返回。注意：只能向上下左右四个方向染色。
#输入样例：
#111111
#111001
#100110
# x = 2, y = 1
#输出样例：
#111111
#111001
#111110

class Solution:
	row = 0
	col = 0

	def fillColor(self, matrix, x, y):
		if not matrix or not x or not y:
			return
		self.row = len(matrix)
		self.col = len(matrix[0])
		self.dfs(matrix, x, y) 

	def dfs(self, matrix, x, y):
		if x < 0 or x >= self.row or y < 0 or y >= self.col or matrix[x][y] != 0:
			return 
		matrix[x][y] = 1
		self.dfs(matrix, x-1, y)
		self.dfs(matrix, x+1, y)
		self.dfs(matrix, x, y-1)
		self.dfs(matrix, x, y+1)

if __name__ == "__main__":
	solu = Solution()
	matrix = [[1,1,1,1,1,1], [1,1,1,0,0,1], [1,0,0,1,1,0]]
	solu.fillColor(matrix, 2, 1)
	print matrix
