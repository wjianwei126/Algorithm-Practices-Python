# http://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=142614&extra=page%3D1%26filter%3Dsortid%26sortid%3D311%26searchoption%255B3046%255D%255Bvalue%255D%3D1%26searchoption%255B3046%255D%255Btype%255D%3Dradio&page=1
class Solution:
    def uglyNumber2Revised(self, nums, k):
        indices = [0] * len(nums)
        res = [1] * (k + 1)
        for i in range(1, k+1):
            nextNum = res[indices[0]] * nums[0]
            for j in range(1, len(nums)):
                nextNum = min(nextNum, res[indices[j]] * nums[j])
            for j in range(len(nums)):
                if nextNum ==  res[indices[j]] * nums[j]:
                    indices[j] += 1
            res[i] = nextNum
        return res[1:]

solu = Solution()
nums = [2,3,5]
k = 10
print solu.uglyNumber2Revised(nums, k)
