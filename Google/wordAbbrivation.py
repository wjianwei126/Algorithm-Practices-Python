# http://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=140866&extra=page%3D1%26filter%3Dsortid%26sortid%3D311%26searchoption%5B3046%5D%5Bvalue%5D%3D1%26searchoption%5B3046%5D%5Btype%5D%3Dradio%26sortid%3D311
#  word abbreviation, 版上之前也有人发过. 一个string只保留首尾字母, 中间字母数用数字表示,
# 比如 "abcde" = "a3e", "ab" = "ab", "abc" = "a1c" . 给一组string, 输出相同abbreviation的所有string, 但重复的string不算.
# 直接用的hashmap, 存储string的时候脑子没转过来,用的array,面试官问是不是有更好的,果断换hashset.
class Solution:
    def wordAbbrivation(self, strings):
        if not strings: return []
        dic = {}

        def toAbbrivation(s):
            if len(s) < 3: return s
            return s[0] + str(len(s)-2) + s[len(s)-1]

        for s in strings:
            abbr = toAbbrivation(s)
            if abbr in dic:
                if s not in dic[abbr]:
                    dic[abbr].add(s)
            else:
                dic[abbr] = set()
                dic[abbr].add(s)

        for abbrSets in dic.values():
            if len(abbrSets) > 1:
                return list(abbrSets)
        return []

solu = Solution()
strings = ['abcde', 'ab', 'abc', 'abc', 'acc', 'asdfse']
print solu.wordAbbrivation(strings)
