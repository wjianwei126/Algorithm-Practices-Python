class Solution:
    def firstMissingPositive(self, nums):
        if not nums: return 1
        i = 0
        while i < len(nums):
            if nums[i] <= 0 or nums[i] > len(nums) or nums[i] == i + 1 or nums[i] == nums[nums[i]-1]:
                i += 1
            else:
                index = nums[i]
                nums[i], nums[index-1] = nums[index-1], nums[i]
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return i + 2

solu = Solution()
nums = [1,6,3,5]
print solu.firstMissingPositive(nums)
