class Solution:
    def encodeStringWays(self, s):
        if not s: return []
        if len(s) == 1: return [s, '1']
        res = []

        remain = self.encodeStringWays(s[1:])
        for way in remain:
            res.append(s[0] + way)

        res.append(str(len(s)))

        for i in range(1, len(s)):
            remain = self.encodeStringWays(s[i:])
            for way in remain:
                res.append(str(i) + way)
        return res

solution = Solution()
s = 'abc'
print solution.encodeStringWays(s)
