# given an array with unique prime numbers, return all the possible products from the array
# each number can be used for only once
# e.g. input [2,3,5] output [2,3,5,6,10,15,30]

class Solution:
	def allProducts(self, A):
		if not A or len(A) == 0: return []
		re = []
		for i in range(1<<len(A)):
			product = 1
			for j in range(len(A)):
				if i&(1<<j) != 0:
					product *= A[j]
			re.append(product)
		return re

	def recursive(self, A):
		if not A or len(A) == 0: return [1]
		subsets = self.recursive(A[1:])
		re = subsets + [A[0]*sets for sets in subsets]
		return re

	def dupRecurSolu(self, A):
		A.sort()
		subsets = self.dupRecursive(A)
		re = []
		for sets in subsets:
			product = 1
			for num in sets:
				product *= num
			re.append(product)
		return re

	def dupRecursive(self, A):
		"The input array can have duplicated item"
		if not A or len(A) == 0: return [[]]
		subsets = self.dupRecursive(A[1:])
		if (len(A) > 1 and A[0] == A[1]):
			re = subsets + [[A[0]] + sets for sets in subsets if (([A[0]] + sets) not in subsets)]
		else:
			re = subsets + [[A[0]] + sets for sets in subsets]
		return re


if __name__ == "__main__":
	solu = Solution()
	A = [2,3,2]
	print solu.allProducts(A)
	print solu.recursive(A)
	print solu.dupRecurSolu(A)
