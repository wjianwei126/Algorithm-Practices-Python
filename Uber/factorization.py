class Solution:
    def factorization(self, number):
        if number <= 0: return []
        self.number = number
        return self.helper(number, number)

    def helper(self, number, start):
        if number == 1: return [[1]]
        res = []
        for i in range(start, 1, -1):
            if number % i == 0:
                remain = self.helper(number/i, i)
                for combine in remain:
                    if combine == [1] and i != self.number:
                        res.append([i])
                    else:
                        res.append([i] + combine)
        return res


solution = Solution()
print solution.factorization(100)
# print solution.factorization
