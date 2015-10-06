# http://www.1point3acres.com/bbs/thread-141438-1-1.html
class Solution:
    def binaryWatch(self, n):
        if n == 0: return ['0:00']
        if n > 8: return []
        res = []
        for upLight in range(min(n+1, 4)):
            downLight = n - upLight
            hours = self.getTime(upLight, 4)
            minutes = self.getTime(downLight, 6)
            for h in hours:
                for m in minutes:
                    if h <= 11 and m <= 59:
                        m = str(m) if m >= 10 else '0'+str(m)
                        res.append(str(h)+':'+m)
        return res

    def getTime(self, number, totalDigits):
        if number == 0: return [0]
        if number > totalDigits: return []

        res = []

        if number == 1:
            for i in range(totalDigits):
                res.append(1<<i)
            return res

        for i in range(totalDigits)[::-1]:
            cur = 1 << i
            for remain in self.getTime(number-1, i):
                res.append(cur + remain)

        return res

solu = Solution()
print solu.binaryWatch(8)
