class Solution:
    def sepOddEven(self, nums):
        if not nums or len(nums) == 0: return None
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] % 2 == 0:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            else:
                left += 1
        return nums

if __name__ == '__main__':
    solu = Solution()
    nums = [1,2,3,4,5,6]
    print solu.sepOddEven(nums)
