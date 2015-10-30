import random
class Solution:
    def findKth(self, nums, k):
        if k > len(nums): return None
        left, pivot, right = self.partition(nums)
        if len(right) == k - 1:
            return pivot
        elif len(right) < k - 1:
            res = self.findKth(left, k - len(right) - 1)
        else:
            res = self.findKth(right, k)
        return res

    def partition(self, nums):
        index = random.randint(0, len(nums)-1)
        nums[0], nums[index] = nums[index], nums[0]
        pivot = nums[0]
        left = []
        right =[]
        for i in range(1, len(nums)):
            if nums[i] <= pivot:
                left.append(nums[i])
            else:
                right.append(nums[i])
        return left, pivot, right

solution = Solution()
nums = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print solution.findKth(nums, 4)
