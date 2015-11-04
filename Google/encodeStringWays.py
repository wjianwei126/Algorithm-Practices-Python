# 给一个字符串，连续的字符可以用数字替代，比如 "school"
# 可以缩写成 “sch3” "s4l" "s5" "s1h2l", 求所有可能的缩写
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
