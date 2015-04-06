# given an array, move a certain number to the left and move another certain number to the right
# the rest order should not be changed
# e.g. input [0,1,0,0,2,3,9,0,4,9,9,5,0,6,9,7,8,9] move all 0 to left and all 9 to right
# output [0,0,0,0,0,1,2,3,4,5,6,7,8,9,9,9,9,9]

class Solution:
	def stableSortColor(self, S):
		if not S or len(S) == 0:
			return []
		left = 0
		right = len(S) - 1
		cur = 0
		while cur <= right:
			if S[cur] == 0:
				i = cur-1
				while i >= left:
					S[i+1] = S[i]
					i -= 1
				S[left] = 0
				left += 1
				cur += 1
			elif S[cur] == 9:
				i = cur
				while i < right:
					S[i] = S[i+1]
					i += 1
				S[right] = 9
				right -= 1
			else:
				cur += 1
		return S

if __name__ == "__main__":
	solu = Solution()
	S = [0,1,0,0,2,3,9,0,4,9,9,5,0,6,9,7,8,9]
	print solu.stableSortColor(S)