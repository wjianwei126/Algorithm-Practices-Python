class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0: return 0
        if len(nums) == 1: return 1
        cur = 1
        new = 0
        dup = False
        while cur < len(nums):
            if nums[cur] == nums[cur-1]:
                if dup:
                    while cur < len(nums) and nums[cur] == nums[cur-1]:
                        cur += 1
                    dup = False
                else:
                    dup = True
                    new += 1
                    nums[new] = nums[cur]
                    cur += 1
            else:
                new += 1
                nums[new] = nums[cur]
                cur += 1
        return new + 1

if __name__ == '__main__':
    solu = Solution()
    nums = [1, 1, 1]
    print solu.removeDuplicates(nums)
