# 给两个string s跟p，问如何判断p是不是s的某个substring的permutation，例如s = "dlwercxhhcd", p = "hdch"，返回true
class Solution:
    def substringPermu(self, s, p):
        if not s or len(s) < len(p): return False
        dic = {}
        count = {}
        for ch in p:
            dic[ch] = dic.get(ch, 0) + 1
            count[ch] = count.get(ch, 0) + 1
        missing = len(p)
        left = right = 0
        while right < len(s):
            if s[right] not in dic:
                for ch in dic:
                    count[ch] = dic[ch]
                missing = len(p)
                right += 1
                left = right
                continue
            if count[s[right]] == 0:
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
                    return True
                right += 1
        return False


solution = Solution()
s = 'abcdefe'
p = 'cef'
s = 'abcbbefefc'
p = 'cef'
print solution.substringPermu(s, p)
