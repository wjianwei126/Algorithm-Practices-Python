class Solution:
    def sqrt(self, x, k):
        if x < 0: return -1
        if x == 0: return 0
        x = x * 1.0
        r = x
        pre = -1
        while r * r > x:
            r = (r + x / r) / 2.0
            if pre == -1:
                pre = r
                continue
            else:
                if pre * pow(10, k) == r * pow(10, k):
                    break
                pre = r
        return int(r * pow(10, k)) / float(pow(10, k))

solu = Solution()
x = 5
print solu.sqrt(x, 4)
