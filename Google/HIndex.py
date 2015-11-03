# given an array, output a maximum k such that there are k elements larger
# than the value k.
class Solution:
    def HIndex(self, nums):
        # O(nlogn)
        if not nums: return 0
        nums.sort()
        i = len(nums) - 1
        res = 0
        while i >= 0:
            if nums[i] > res + 1:
                res += 1
                i -= 1
            else:
                break
        return res

    def HIndex2(self, nums):
        # O(n) time O(n) space
        if not nums: return 0
        countList = [0] * (len(nums) + 1)
        for num in nums:
            if num >= len(nums):
                countList[len(nums)] += 1
            elif num <= 0:
                countList[0] += 1
            else:
                countList[num] += 1
        i = len(countList) - 1
        res = 0
        while i >= 0:
            if res + countList[i] < i:
                res += countList[i]
                i -= 1
            else:
                return res
        return 0

solution = Solution()
nums = []
nums = [-1,-2,-3]
# nums = [5,9,6,-1,0,2,5,-23]
print solution.HIndex(nums), solution.HIndex2(nums)
