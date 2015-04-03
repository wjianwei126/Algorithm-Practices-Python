# sparse dot product
# A =[0,2,0,2,0,0,3,0,0,4]
# B=[0,0,0,0,5,0,2,0,0,8]
# output 38
class Solution:
	def sparseDotProduct(self, A, B):
		if not A or not B: return 0
		a_nonZ = {}
		for i in range(len(A)):
			if A[i] != 0:
				a_nonZ[i] = A[i]
		b_nonZ = {}
		for i in range(len(B)):
			if B[i] != 0:
				b_nonZ[i] = B[i]

		sum = 0

		for index in a_nonZ.keys():
			if index in b_nonZ:
				sum += a_nonZ[index] * b_nonZ[index]
		return sum

if __name__ == "__main__":
	solu = Solution()
	A = [0,2,0,2,0,0,3,0,0,4]
	B = [0,0,0,0,5,0,2,0,0,8]
	print solu.sparseDotProduct(A, B)