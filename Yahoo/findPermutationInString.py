class Solution:
    def findPermutationInString(self, s, permu):
        if not s or not permu: return -1
        if len(s) < len(permu): return -1
        dic = {}
        count = {}
        for ch in permu:
            dic[ch] = dic.get(ch, 0) + 1
            count[ch] = count.get(ch, 0) + 1
        missing = len(permu)
        left = right = 0
        res = []
        while right < len(s) and left < len(s) - len(permu) + 1:
            if s[right] not in dic:
                right += 1
                left = right
                count = dic
                missing = len(permu)
                continue
            if count[s[right]] == 0:
                print left
                while s[left] != s[right]:
                    count[s[left]] += 1
                    missing += 1
                    left += 1
                left += 1
                right += 1
            else:
                count[s[right]] -= 1
                missing -= 1
                if missing == 0:
                    res.append(left)
                    count[s[left]] += 1
                    missing += 1
                    left += 1
                right += 1

        return res

solution = Solution()
s = 'abcdcbabca'
permu = 'abc'
s = 'aaaaa'
permu = 'a'
print solution.findPermutationInString(s, permu)
