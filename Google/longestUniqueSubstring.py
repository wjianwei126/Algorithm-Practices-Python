# Find the longest substring in an input string,
# such that there are at most k unique characters in the substring

class Solution:
    def longestUniqueSubstring(self, s, k):
        if not s: return ''
        missing = k
        dic = {}
        res = s[0]
        left = right = 0
        while right < len(s):
            if s[right] in dic:
                dic[s[right]] += 1
                right += 1
            else:
                if missing == 0:
                    res = s[left:right] if right - left > len(res) else res
                    dic[s[left]] -= 1
                    if dic[s[left]] == 0:
                        del dic[s[left]]
                        missing += 1
                    left += 1
                else:
                    dic[s[right]] = 1
                    missing -= 1
                    right += 1

        res = s[left:right] if right - left > len(res) else res
        return res

solu = Solution()
s = 'abbcaddddefc'
print solu.longestUniqueSubstring(s, 3)
