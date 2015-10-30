# word break, but only return one combination
class Solution:
    def wordBreak(self, wordDict, s):
        if not s or not wordDict: return []
        self.path = None
        self.helper(wordDict, s, [])
        return self.path

    def helper(self, wordDict, s, path):
        if self.path:
            return
        for word in wordDict:
            if len(word) > len(s):
                continue
            i = 0
            while i < len(word) and word[i] == s[i]:
                i += 1
            if i == len(word):
                if i == len(s):
                    self.path = path + [word]
                    return
                wordDict.remove(word)
                self.helper(wordDict, s[i:], path + [word])
                wordDict.add(word)

solution = Solution()
wordDict = set(['cat', 'cats', 'and', 'sand', 'dog'])
s = 'catsanddog'
print solution.wordBreak(wordDict, s)
