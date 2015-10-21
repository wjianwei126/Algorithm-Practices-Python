class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        if not wordDict:
            return []
        # self.find = False
        words = self.helper(wordDict, s)
        res = []

        for word in words:
            temp = ' '.join(word)
            res.append(temp)
        return res

    def helper(self, dic, s):
        if not dic: return [[]]
        if not s:
            # self.find = True
            return [[]]
        res = []
        words = []
        for i in dic:
            words.append(i)
        for word in words:
            # if self.find:
            #     break
            i = 0
            while i < len(word):
                if i >= len(s) or s[i] != word[i]:
                    break
                i += 1
            if i == len(word):
                temp = [word]
                dic.remove(word)
                remain = self.helper(dic, s[i:])
                for solu in remain:
                    res.append(temp + solu)
                dic.append(word)

        return res

solution = Solution()
s = 'catsanddog'
wordDict = ["cat", "cats", "and", "sand", "dog"]
print solution.wordBreak(s, wordDict)
