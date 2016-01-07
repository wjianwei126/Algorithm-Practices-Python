def longestConsective(nums):
    if not nums: return 0
    if len(nums) == 1: return 1

    curLongest = 1
    curLen = 1
    curDiff = nums[1] - nums[0]
    for i in range(1, len(nums)):
        if nums[i] - nums[i-1] == curDiff:
            curLen += 1
        else:
            curLongest = max(curLongest, curLen)
            curDiff = nums[i] - nums[i-1]
            curLen = 2
    curLongest = max(curLongest, curLen)
    return curLongest

nums = [1,2,3,4,5,8,11]
nums = [1]
nums = [1, 2, 3, 5, 3, 5, 7, 9, 11, 10]
print longestConsective(nums)

maxLen = 0

def update(dp, diff, length):
    global maxLen
    if diff not in dp or dp[diff] < length:
        dp[diff] = length
        maxLen = max(maxLen, length)

def longestUnconsectiveAP(nums):
    if not nums: return 0
    if len(nums) <= 2: return len(nums)

    dp = {}
    for i in range(len(nums)):
        dp[i] = {}

    for i in range(1, len(nums)):
        for j in range(i):
            diff = nums[i] - nums[j]
            if diff in dp[j]:
                update(dp[i], diff, dp[j][diff] + 1)
            else:
                update(dp[i], diff, 2)
    print dp

nums = [1, 3, 5, 10, 10, 7, 2, 4, 9, 1, -2, 11]
longestUnconsectiveAP(nums)
print maxLen
