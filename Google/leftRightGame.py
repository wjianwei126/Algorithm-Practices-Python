class Solution:
    def leftRightGame(self, nums):
        if not nums: return 0
        return self.helper(nums)[1]

    def helper(self, nums):
        if not nums: return (True, 0)
        if len(nums) == 1:
            return (True, nums[0])
        choice1 = self.helper(nums[1:])[0]
        if choice1:
            leftVal = nums[0] + self.helper(nums[2:])[1]
        else:
            leftVal = nums[0] + self.helper(nums[1:len(nums)-1])[1]

        choice2 = self.helper(nums[:-1])[0]
        if choice2:
            rightVal = nums[-1] + self.helper(nums[1:len(nums)-1])[1]
        else:
            rightVal = nums[-1] + self.helper(nums[:-2])[1]

        return (leftVal > rightVal, max(leftVal, rightVal))

solution = Solution()
nums = [1,1,8,2,3,4,4]
print solution.leftRightGame(nums)
