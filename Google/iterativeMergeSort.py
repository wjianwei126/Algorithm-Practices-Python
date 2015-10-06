class Solution:
    def mergeSort(self, nums):
        if not nums: return nums
        self.nums = nums
        curSize = 1
        leftStart = 0
        length = len(self.nums)
        while curSize < length:
            leftStart = 0
            while leftStart < length - 1:
                mid = leftStart + curSize - 1
                rightEnd = leftStart + 2 * curSize - 1
                self.merge2(leftStart, mid, rightEnd)
                leftStart += curSize * 2
            curSize *= 2
        return self.nums

    def merge(self, left, mid, right):
        right = min(len(self.nums)-1, right)
        if mid == left or mid == right: return
        i = mid
        while i <= right:
            j = i
            x = self.nums[i]
            while j > 0 and self.nums[j-1] >= x:
                self.nums[j] = self.nums[j-1]
                j -= 1
            self.nums[j] = x
            i += 1

solu = Solution()
nums = [5,7,6,4,3,2,5,8,1,10]
print solu.mergeSort(nums)
