# Given a list and a target, output whether or not the target can be the combination of elements in the list. 
# The elements can be used more than once

class Solution:
	def combinationSum(self, increments, target):
		if len(increments) == 0:
			return False
		increments.sort()
		return self.partSum(increments, target)

	def partSum(self, increments, target):
		re = []
		for i in range(len(increments)):
			if increments[i] < target:
				temp = self.partSum(increments[i:], target - increments[i])
				for comb in temp:
					re.append([increments[i]] +  comb)
			elif increments[i] == target:
				re.append([increments[i]])
				return True
			else:
				break
		return True

if __name__ == "__main__":
	solu = Solution()
	increments1, target1 = [3, 2, 3, 7], 11
	increments2, target2 = [10,2,7,6,5], 1
	print solu.combinationSum(increments1, target1)
