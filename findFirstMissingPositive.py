class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 1
        i = 0
        while i < len(nums):
            if nums[i] > len(nums) or nums[i] <= 0 or nums[i] == i + 1 or nums[i] == nums[nums[i]-1]:
                i += 1
            else:
                temp = nums[i]
                nums[i], nums[temp-1] = nums[temp-1], nums[i]
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return i + 2

if __name__ == '__main__':
    solu = Solution()
    nums = [1]
    print solu.firstMissingPositive(nums)
