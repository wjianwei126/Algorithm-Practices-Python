# Given a list and a target, output whether or not the target can be the combination of elements in the list. 
# The elements can be used more than once

class Solution:
	def combinationSum(self, increments, target):
		increments.sort()
		return self.partSum(increments, target)

	def partSum(self, increments, target):
		for i in range(len(increments)):
			if increments[i] < target:
				return self.partSum(increments[i:], target - increments[i])
			elif increments[i] == target:
				return True
			else:
				break
		return False

if __name__ == "__main__":
	solu = Solution()
	increments1, target1 = [10,1,2,7,6,1,5], 8
	increments2, target2 = [10,2,7,6,5], 1
	print solu.combinationSum(increments2, target2)
