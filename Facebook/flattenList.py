# flatten a list

class Solution:
	def flattenList(self, L):
		if not L or len(L) == 0: return []
		i=0
		re = []
		for i in range(len(L)):
			if isinstance(L[i], list):
				re += self.flattenList(L[i])
			else:
				re.append(L[i])
		return re

		
	def flatten(self, lst):
		return sum( ([x] if not isinstance(x, list) else self.flatten(x) for x in lst), [] )


if __name__ == "__main__":
	solu = Solution()
	L = [[1], 2, [[3,4], 5], [[[]]], [[[6]]], 7, 8, []]
	#print solu.flatten(L)
	print solu.flattenList(L)