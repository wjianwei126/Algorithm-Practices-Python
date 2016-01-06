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
