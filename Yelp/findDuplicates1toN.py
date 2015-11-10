# "一个array的range是1-N，这个array里有1+N个数, 找出这个array里的duplicate。(ex. [1, 1, 3, 5])   HashMap 解决
# 然后条件升级, 问不能用extra space。                                                                                                想了一下, 先sort, 再找
# 再升级, 不能改变array, 不能有extra space。"
class Solution:
    def findDuplicates1(self, nums, N):
        # O(n) time O(n) space
        if N < 1: return -1
        if N == 1: return 1
        numSet = set()
        for num in nums:
            if num in numSet:
                return num
            else:
                numSet.add(num)

    def findDuplicates2(self, nums, N):
        # O(nlogn) time O(1) space
        if N < 1: return -1
        if N == 1: return 1
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]

    def findDuplicates3(self, nums, N):
        # O(n) time O(1) space
        if N < 1: return -1
        if N == 1: return 1
        i = 0
        while i < len(nums):
            if nums[i] != i + 1:
                if nums[nums[i] - 1] == nums[i]:
                    return nums[i]
                else:
                    temp = nums[i] - 1
                    nums[i], nums[temp] = nums[temp], nums[i]
            else:
                i += 1

    def findDuplicates4(self, nums, N):
        # O(nlogn) time O(1) space without modifying the array
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) / 2
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            if count <= mid:
                left = mid + 1
            else:
                right = mid
        return left
solution = Solution()
nums = [1,1,1,3]
nums = [5, 7, 6, 4, 3, 6, 2, 1]
print solution.findDuplicates1(nums, 7)
print solution.findDuplicates2(nums, 7)
print solution.findDuplicates3(nums, 7)
print solution.findDuplicates4(nums, 7)
