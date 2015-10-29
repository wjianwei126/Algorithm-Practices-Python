class Solution:
    def maxExpression(self, nums):
        if not nums: return None
        if len(nums) == 1: return nums[0]
        dp = [[0] * len(nums) for x in range(len(nums))]
        for i in range(len(nums)):
            dp[i][i] = nums[i]
        begin = 1
        i, j = 0, begin
        while j < len(nums):
            for k in range(i, j):
                dp[i][j] = max(dp[i][j], dp[i][k] + dp[k+1][j], dp[i][k] * dp[k+1][j])
            i += 1
            j += 1
            if j == len(nums):
                begin += 1
                i, j = 0, begin
        return dp[0][len(nums)-1]

    def maxExpressionWithNegative(self, nums):
        if not nums: return None
        if len(nums) == 1: return nums[0]
        maxDP = [[float('-inf')] * len(nums) for x in range(len(nums))]
        minDP = [[float('inf')] * len(nums) for x in range(len(nums))]
        for i in range(len(nums)):
            maxDP[i][i] = nums[i]
            minDP[i][i] = nums[i]
        begin = 1
        i, j = 0, begin
        while j < len(nums):
            for k in range(i, j):
                maxDP[i][j] = max(maxDP[i][j], maxDP[i][k] + maxDP[k+1][j], minDP[i][k] * minDP[k+1][j], maxDP[i][k] * maxDP[k+1][j], minDP[i][k] * maxDP[k+1][j], maxDP[i][k] * minDP[k+1][j])
                minDP[i][j] = min(minDP[i][j], minDP[i][k] + minDP[k+1][j], minDP[i][k] * minDP[k+1][j], maxDP[i][k] * maxDP[k+1][j], minDP[i][k] * maxDP[k+1][j], maxDP[i][k] * minDP[k+1][j])
            i += 1
            j += 1
            if j == len(nums):
                begin += 1
                i, j = 0, begin
        return maxDP[0][len(nums)-1]
solution = Solution()
nums = [1,0,-2,-1]
# nums = [1,4,6,1,2]
# print solution.maxExpression(nums)
print solution.maxExpressionWithNegative(nums)
