# given an array with positive and negative numbers
# return a subsequence of length k with maximum product

class Solution:
	def maxProductSeq(self, A, k):
		def cmp(x, y):
			if x > 0 and y > 0:
				cmp(-x, -y)
			elif x > 0 and y < 0:
				return -1
			elif x < 0 and y > 0:
				return 1
			elif x == 0:
				return -1
			elif y == 0:
				return 1
		A.sort(cmp)
		print A


if __name__ == "__main__":
	solu = Solution()
	A = [23, -43, 0, 5, 93, -5, -37]
	solu.maxProductSeq(A, 5)
