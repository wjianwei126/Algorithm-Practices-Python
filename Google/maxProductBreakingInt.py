# 将一个正整数分成若干个数的和，求这些数的最大乘积
class Solution:
    def maxProductBreakingInt(self, n):
        # O(n^2)
        if n <= 0: return 0
        if n == 1: return 1
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n+1):
            for j in range(1, i/2+1):
                dp[i] = max(dp[i], dp[j] * dp[i-j])
            dp[i] = max(dp[i], i)
        return dp[n]

    def maxProductBreakingInt2(self, n):
        # O(n)
        if n <= 0: return 0
        if n == 1: return 1
        if n == 2: return 2
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2
        dp[3] = 3
        for i in range(4, n+1):
            dp[i] = max(2 * dp[i - 2], 3 * dp[i - 3])
        return dp[n]

    def maxProductBreakingInt3(self, n):
        if n <= 0: return 0
        if n == 1: return 1
        if n == 2: return 2
        res = 1
        while n > 0:
            if n >= 5:
                res *= 3
                n -= 3
                continue
            if n == 4:
                res *= 4
                break
            if n == 3:
                res *= 3
                break
            if n == 2:
                res *= 2
                break
        return res

solution = Solution()
for i in range(1, 20):
    print solution.maxProductBreakingInt(i), solution.maxProductBreakingInt2(i), solution.maxProductBreakingInt3(i)
