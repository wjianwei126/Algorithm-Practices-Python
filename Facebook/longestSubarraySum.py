# A maximum sized Subsequence, sum is a given number
# e.g. input [5, 3, 6, 5, -2, 7, -4, 5], 14 ouput (3,6,5) => 3

class Solution:
    def LongSub(self, num, target):
        "O(n) time O(n) space"
        if not num or len(num) == 0: return 0
        _dict = {}
        _sum = 0
        maxsofar = 0
        _dict[0] = -1
        for i in range(len(num)):
            _sum += num[i]
            if _sum not in _dict:
                _dict[_sum] = i
            if _sum - target in _dict:
                index = _dict[_sum - target]
                maxsofar = max(maxsofar, i - index)
        
        return maxsofar

if __name__ == "__main__":
    solu = Solution()
    num = [5, 3, 6, 5, -2, 7, -5, 0, 5]
    print solu.LongSub(num, 14)