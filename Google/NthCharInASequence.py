# 问的是给一个无穷的sequence, ABCAABBCCAAAABBBBCCCC... 每次A,B,C数量double, 
# 然后问给一个正整数n, 求第n个char是什么
# 第一个是A, 第二个是B, 以此类推...
# 这题一开始我就想把通项公式求出来,然后分不同的sequence做,然后一直卡在一个地方.
# 小哥提醒先用最简单的方法, 然后写出O(n) 算法, 之后我就知道怎么优化, 用binary search
# 求出最后一个k 使得 3 * (pow(2, k)) < n
# 然后从这个数字开始搜索, 这样最好的running time 是O(log(n))
class Solution:
    def findNthChar(self, n):
        if n <= 0: return ''
        dic = {0: 'A', 1: 'B', 2: 'C'}
        count = 0
        k = 0
        while count + 3 * (2 ** k) < n:
            count += 3 * (2 ** k)
            k += 1
        recur = 2 ** k
        remain = n - count
        index = (remain-1) / recur
        return dic[index]

solution = Solution()
for i in range(1, 20):
    print solution.findNthChar(i)
