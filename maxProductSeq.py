# given an array with positive and negative numbers
# return a subsequence of length k with maximum product

class Solution:
	def maxProductSeq(self, A, k):
		if not A or len(A) == 0: return 0
		if len(A) <= k: 
			return productor(A)

		def productor(s):
			prod = 1
			for i in range(len(s)):
				prod *= s[i]
			return prod

		def comperator(x, y):
			if x > 0 and y > 0:
				return y-x
			elif x > 0 and y < 0:
				return 1
			elif x < 0 and y > 0:
				return -1
			elif x < 0 and y < 0:
				return y-x
			elif x == 0:
				return 1
			elif y == 0:
				return -1
		A.sort(cmp = comperator)

		i = 0
		while i < len(A):
			if A[i] < 0:
				i += 1
			else:
				break

		left = i

		if len(A) - i >= k:
			left = i		
		else:
			if (k - (len(A) - i))%2 == 1:
				left = left - (k - (len(A) - i)) - 1
			else:
				left = left - (k - (len(A) - i))

		right = left + k - 1

		while left - 2 >= 0 and A[left-1]*A[left-2] > A[right-1]*A[right]:
			left -= 2
			right -= 2

		return productor(A[left:right+1])



if __name__ == "__main__":
	solu = Solution()
	A = [23, -43, 0, 5, 93, -5, -37]
	print solu.maxProductSeq(A, 5)
