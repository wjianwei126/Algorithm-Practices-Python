class Solution:
    def shortestStrContainAllPasscode(self):
        visited = set()
        num = 0
        res = '000'
        while len(visited) < 10000:
            res += str(num % 10)
            visited.add(num)
            num = num % 1000 * 10

            count = 0
            while count < 9:
                if num + count not in visited:
                    break
                count += 1

            num += count

        return res

solution = Solution()
s = solution.shortestStrContainAllPasscode()
for i in range(10000):
    if str(i) not in s:
        print 'fuck'
print s
