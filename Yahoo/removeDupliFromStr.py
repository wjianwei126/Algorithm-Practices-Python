class Solution:
    def removeDupliFromStr(self, s):
        if not s: return ''
        s = list(s)
        letters = set()
        left = right = 0
        while right < len(s):
            if s[right] not in letters:
                s[left] = s[right]
                letters.add(s[right])
                left += 1
                right += 1
            else:
                right += 1
        return ''.join(s[:left])

solution = Solution()
s = 'abracadabra'
print solution.removeDupliFromStr(s)
