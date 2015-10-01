# Given an array, randomly return one of its maximum valuse
# e.g. [1,2,3,3,3,3,1,2] randomly return one of the index among the four 3s
from random import randint
class Solution:
	def maxRandom(self, A):
		if not A or len(A) == 0: return 
		maxsofar = A[0]
		index = [0]
		for i in range(len(A)):
			if A[i] == maxsofar:
				index.append(i)
			elif A[i] > maxsofar:
				maxsofar = A[i]
				index = [i]
		if len(index) == 1:
			return index[0]
		return index[randint(0, len(index)- 1)]

if __name__ == "__main__":
	solu = Solution()
	A = [1,2,3,3,3,3,1,2]
	print solu.maxRandom(A)