import math
class Solution:
    def HVpermutation(self, x, y, k):
        if k < 0: return ''
        res = ''
        n = x + y
        while n > 0:
            remain = math.factorial(n-1) / (math.factorial(x) * math.factorial(y-1))
            index = k / remain
            if index == 0:
                res += 'H'
                y -= 1
                k = k % remain
            else:
                res += 'V'
                x -= 1
                k = k - remain
            n -= 1
            if k == 0:
                res += 'H' * y + 'V' * x
                break

        return res

solution = Solution()
for i in range(6):
    print solution.HVpermutation(0, 2, i)
