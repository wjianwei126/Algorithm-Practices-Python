class Solution:
    def numberPalin(self, level):
        if level <= 0: return []
        if level == 1: return ['0', '1', '8']
        if level == 2: return ['11', '88', '25', '52', '69', '96']
        dp = [[] for x in range(level+1)]
        dp[1] = ['0', '1', '8']
        dp[2] = ['00', '11', '88', '25', '52', '69', '96']
        base = ['11', '88', '25', '52', '69', '96']
        for k in range(3, level):
            for num in dp[2]:
                temp = ''
                left = num[0]
                right = num[1]
                for s in dp[k-2]:
                    temp = left + s + right
                    dp[k].append(temp)
        for num in base:
            temp = ''
            left = num[0]
            right = num[1]
            for s in dp[level-2]:
                temp = left + s + right
                dp[level].append(temp)
        return dp[level]

solution = Solution()
print solution.numberPalin(5)
