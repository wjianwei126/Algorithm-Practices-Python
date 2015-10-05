# find numbers appears more than n/4 times
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums: return []
        candidates = [None, None, None]
        count = [0, 0, 0]
        for number in nums:
            findCan = False
            for i in range(len(candidates)):
                if number == candidates[i]:
                    count[i] += 1
                    findCan = True
            if findCan: continue

            replaceCan = False
            for i in range(len(count)):
                if count[i] == 0:
                    candidates[i] = number
                    count[i] = 1
                    replaceCan = True
                    break
            if replaceCan: continue

            for i in range(len(count)):
                count[i] -= 1

        res = []
        count = [0, 0, 0]
        for number in nums:
            for i in range(len(candidates)):
                if number == candidates[i]:
                    count[i] += 1
        for i in range(len(candidates)):
            if count[i] > len(nums) / 4: res.append(candidates[i])
        return res

solu = Solution()
nums = [1,1,2,3,2,2,2,2,4,4,5,4,1,1]
print solu.majorityElement(nums)
