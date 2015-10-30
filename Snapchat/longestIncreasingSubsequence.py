class Solution:
    def longestIncreasingSubsequence(self, nums):
        if not nums: return 0
        if len(nums) == 1: return 1
        dp = [0] * len(nums)
        dp[0] = 1
        for i in range(1, len(nums)):
            temp = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    temp = max(temp, 1+dp[j])
            dp[i] = temp
        return dp[-1]

solution = Solution()
nums = [10, 20, 9, 33, 21, 50, 41, 60, 80]
print solution.longestIncreasingSubsequence(nums)
