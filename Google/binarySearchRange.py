class Solution:
    def searchRange(self, downLine, upLine, nums):
        if not nums or downLine > upLine: return 0
        if downLine > nums[-1] or upLine < nums[0]: return 0
        if downLine < nums[0]:
            downMark = 0
        else:
            downMark = self.binarySearch(nums, downLine, True)
        if upLine > nums[-1]:
            upMark = len(nums) - 1
        else:
            upMark = self.binarySearch(nums, upLine, False)

        return nums[downMark:upMark+1]

    def binarySearch(self, nums, target, ceiling):
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left) / 2
            if nums[mid] == target:
                i = mid
                if ceiling:
                    while i < len(nums) and nums[i] == nums[mid]:
                        i += 1
                else:
                    while i >= 0 and nums[i] == nums[mid]:
                        i -= 1
                return i
            elif nums[mid] > target:
                right = mid
            else:
                left = mid
        if target > nums[left] and target < nums[right]:
            return right if ceiling else left
        if target == nums[left]:
            i = left
            if ceiling:
                while i < len(nums) and nums[i] == nums[left]:
                    i += 1
            else:
                while i >= 0 and nums[i] == nums[left]:
                    i -= 1
            return i
        if target == nums[right]:
            i = right
            if ceiling:
                while i < len(nums) and nums[i] == nums[right]:
                    i += 1
            else:
                while i >= 0 and nums[i] == nums[right]:
                    i -= 1
            return i
solution = Solution()
nums = [0,0,0,0,0]
down, up = 1, 2
nums = [0,0,0,0,0]
down, up = -2, -1
nums = [0,0,0,0,0]
down, up = -2, 2
nums = [1,2,3,4,5]
down, up = 2, 4
nums = [1,2,3,4,5]
down, up = 2.1, 4.4
nums = [1,2,3,4,4,4]
down, up = 2.1, 4.1
print solution.searchRange(down, up, nums)
