class Solution:
	def deleteDup(self, A):
		if not A or len(A) == 0:
			return 0
		slow = 0
		fast = 1
		while fast < len(A):
			if A[fast] == A[slow]:
				fast += 1
			else:
				slow += 1
				A[slow] = A[fast]
				fast += 1
		return slow

if __name__ == "__main__":
	solu = Solution()
	A = [2, 2, 2, 1, 5, 6, 6, 7, 7]
	print solu.deleteDup(A)
	print A