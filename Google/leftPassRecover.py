class Solution:
    def leftPassRecover(self, nums):
        if not nums: return []
        candidates = range(1, len(nums)+1)
        i = len(nums) - 1
        res = []
        while i >= 0:
            j = nums[i]
            k = len(candidates) - 1
            while j > 0:
                k -= 1
                j -= 1
            res = [candidates[k]] + res
            candidates.remove(candidates[k])
            i -= 1
        return res

nums = [0, 1, 1, 3, 0, 5, 1]
solution = Solution()
print solution.leftPassRecover(nums)
