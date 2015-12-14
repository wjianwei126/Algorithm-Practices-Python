def findSubArrays(nums):
    if not nums: return 0
    dp = [[0] * len(nums) for x in range(len(nums))]
    count = 0
    for i in range(len(nums)):
        dp[i][i] = nums[i] % 3
        if dp[i][i] == 0:
            count += 1

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            dp[i][j] = (dp[i][j-1] + nums[j]) % 3
            if dp[i][j] == 0:
                count += 1

    return count

nums = [1,2,3,5]
print findSubArrays(nums)
