# Good number is a number that is at least two pairs of sum of two cubic numbers
# return all the good numbers that is no more than n
class Solution:
    def goodNum(self, n):
        if n <= 0: return []
        cubics = []
        i = 1
        while pow(i, 3) < n:
            cubics.append(pow(i, 3))
            i += 1

        print cubics
        res = []
        for i in range(1, n+1):
            if self.findTwoMoreCubics(cubics, i):
                res.append(i)
        return res

    def findTwoMoreCubics(self, cubic, number):
        if len(cubic) < 2: return False
        left = 0
        right = len(cubic) - 1
        count = 0
        while left < right:
            sum = cubic[left] + cubic[right]
            if sum == number:
                count += 1
                left += 1
                right -= 1
            elif sum > number:
                right -= 1
            else:
                left += 1

            if count >= 2:
                break
        return count >= 2

solu = Solution()
print solu.goodNum(10000)
