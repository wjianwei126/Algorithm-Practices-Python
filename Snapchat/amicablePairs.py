class Solution:
    def amicablePairs(self, n):
        if n < 1: return []
        visited = set()
        res = []
        for i in range(1, n+1):
            if i in visited:
                continue
            divisors = self.findDivisors(i)
            divSum = sum(divisors)
            if divSum > i:
                checkDivisors = self.findDivisors(divSum)
                if sum(checkDivisors) == i:
                    res.append((i, divSum))
                    visited.add(i)
                    visited.add(divSum)
        return res

    def findDivisors(self, n):
        res = []
        for i in range(1, n/2 + 1):
            if n % i == 0:
                res.append(i)
        return res

solution = Solution()
print solution.amicablePairs(7000)
