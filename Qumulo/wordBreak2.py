class Solution:
    def findDecoding(self, wordDict, s):
        self.find = False
        res = self.helper(wordDict, s)
        return res

    def helper(self, wordDict, s):
        if self.find:
            return []

        if not wordDict:
            return []

        if not s:
            self.find = True
            return [[]]

        words = []
        for word in wordDict:
            words.append(word)

        res = []

        for word in words:
            if len(word) > len(s):
                continue
            i = 0
            while i < len(word) and s[i] == word[i]:
                i += 1
            if i == len(word):
                wordDict.remove(word)
                remain = self.helper(wordDict, s[i:])
                for combine in remain:
                    res.append([word] + combine)
                wordDict.add(word)

        return res

s = 'catsanddog'
wordDict = set(['cat', 'cats', 'sand', 'and', 'dog'])
solution = Solution()
print solution.findDecoding(wordDict, s)
