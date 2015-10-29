class Solution:
    def encodeString(self, s):
        if not s: return ''
        # O(n)
        countDic = {}
        for ch in s:
            countDic[ch] = countDic.get(ch, 0) + 1
        # O(n)
        countList = []
        for ch in countDic:
            countList.append((ch, countDic[ch]))
        # O(nlogn)
        countList.sort(cmp = lambda x, y: y[1] - x[1])
        # O(n)
        encodeDic = {}
        count = 0
        for pair in countList:
            encodeDic[pair[0]] = count * '0' + '1'
            count += 1
        res = ''
        for ch in s:
            res += encodeDic[ch]

        return res

solution = Solution()
s = 'abbabc'
print solution.encodeString(s)
