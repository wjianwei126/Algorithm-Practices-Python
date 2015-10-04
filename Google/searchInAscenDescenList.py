# given a list of elements arranged in ascending and then descending order(e.g. 1,3,5,7,6,4,2),
# write a function to determine if a target number in in this list
class Solution:
    def searchInAscenDescenList(self, nums, target):
        if not nums: return -1
        if len(nums) == 1: return 0 if nums[0] == target else -1
        # first find the peak
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) / 2
            if mid == len(nums)-1 and nums[mid] > nums[mid-1] or \
                mid == 0 and nums[mid] > nums[mid+1] or \
                nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                peak = mid
                break
            elif nums[mid] < nums[mid+1]:
                left = mid + 1
            else:
                right = mid - 1

        leftResult = self.binarySearch(nums[:peak], target, True)
        rightResult = self.binarySearch(nums[peak:], target, False)
        if leftResult != -1:
            return leftResult
        if rightResult != -1:
            return rightResult + peak
        return -1

    def binarySearch(self, nums, target, ascending):
        if not nums: return -1
        if len(nums) == 1: return 0 if nums[0] == target else -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                if ascending:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if ascending:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1

solu = Solution()
nums = [1,3,5,7,9,6,4,2]
nums = [1,3,5,7,9]
nums = [8,7,5,4,3]
print solu.searchInAscenDescenList(nums, 5)
