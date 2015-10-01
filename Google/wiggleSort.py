class Solution:
    def wiggleSort1(self, nums):
        if not nums: return
        for i in range(0, len(nums), 2):
            if i < len(nums) - 1 and nums[i+1] < nums[i]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
        for i in range(1, len(nums), 2):
            if i < len(nums) - 1 and nums[i+1] > nums[i]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
        return nums

    def wiggleSort2(self, nums):
        if not nums: return
        incr = True
        prev = nums[0]
        for i in range(1, len(nums)):
            if (incr and nums[i] >= prev) or (not incr and nums[i] <= prev):
                nums[i-1] = prev
                prev = nums[i]
            else:
                nums[i-1] = nums[i]
            incr = not incr
        nums[i] = prev
        return nums

nums = [3,5,6,7,8,2,1,9,6,5,2]
# nums = [9,3,7,5,8,2,4,1]
solu = Solution()
print solu.wiggleSort2(nums)
