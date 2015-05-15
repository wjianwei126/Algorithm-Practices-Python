# input: an array with 98 entries. values inside are from 1 to 100
# output: the missing two numbers
import random
class Solution:
	def  findMissing(self, L):
		# input checking
		if not L or len(L) == 0:
			return -1

		L = L + ["missing", "missing"]
		i = 0
		while i < len(L):
			if L[i] != "missing" and L[i] != L[L[i]-1]:
				temp = L[i] - 1
				L[i], L[temp] = L[temp], L[i]
			else:
				i += 1

		result = []

		for i in range(len(L)):
			if L[i] == "missing":
				result.append(i+1)

		print result


if __name__ == "__main__":
	Solu = Solution()
	L = random.sample(range(1,101),100)
	LL = L[:98]
	print L[-2:]
	Solu.findMissing(LL)