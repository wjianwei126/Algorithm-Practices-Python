# find first pair, triplet, ... that sums to the target in the array
# first can mean the one with smallest index in the array
class Solution:
    def twoSum(self, nums, target):
        # O(n) time O(n) space
        numTable = {}
        lowestIndex = 0
        pairCandidate = []
        for i in range(len(nums)):
            if target - nums[i] not in numTable:
                numTable[nums[i]] = i
            else:
                if not pairCandidate:
                    pairCandidate = [target-nums[i], nums[i]]
                    lowestIndex = numTable[target-nums[i]]
                else:
                    if numTable[target-nums[i]] < lowestIndex:
                        pairCandidate = [target-nums[i], nums[i]]
                        lowestIndex = numTable[target-nums[i]]
        return pairCandidate

    def threeSum(self, nums, target):
        # O(n^2) time O(n) space
        if not nums or len(nums) < 3: return []
        for i in range(len(nums)):
            temp = self.twoSum(nums[i+1:], target - nums[i])
            if len(temp) > 0:
                return [nums[i]] + temp
        return []

    def fourSum(self, nums, target):
        # O(n^2) time O(n) space
        if not nums or len(nums) < 4: return []
        indexedNums = []
        for i in range(len(nums)):
            indexedNums.append((nums[i], i))

        indexedNums.sort(key=lambda x: x[0])

        sumTable = {}
        lowestIndex = 0
        quadrupletCandidate = []
        for i in range(len(indexedNums)-1):
            for j in range(i+1, len(indexedNums)):
                tempSum = indexedNums[i][0] + indexedNums[j][0]
                if target - tempSum in sumTable:
                    for (x, y) in sumTable[target-tempSum]:
                        if y < i:
                            if len(quadrupletCandidate) > 0:
                                curIndex = min(indexedNums[x][1], indexedNums[y][1], indexedNums[i][1], indexedNums[j][1])
                                if curIndex < lowestIndex:
                                    quadrupletCandidate = [indexedNums[x][0], indexedNums[y][0], indexedNums[i][0], indexedNums[j][0]]
                                    lowestIndex = curIndex
                            else:
                                lowestIndex = min(indexedNums[x][1], indexedNums[y][1], indexedNums[i][1], indexedNums[j][1])
                                quadrupletCandidate = [indexedNums[x][0], indexedNums[y][0], indexedNums[i][0], indexedNums[j][0]]
                if tempSum in sumTable:
                    sumTable[tempSum].append((i, j))
                else:
                    sumTable[tempSum] = [(i, j)]
        return quadrupletCandidate


solution = Solution()
nums = [7,4,2,3,1]
target = 5
print solution.twoSum(nums, target)
nums = [7,6,3,5,8,2]
target = 13
print solution.threeSum(nums, target)
nums = [7,6,3,5,8,2,9]
target = 19
print solution.fourSum(nums, target)
