# given a dictionary with many words. 
# return the longest word that can be broken into other words in the dictionary
# if there is no such word, return -1
# e.g. input [face, book, facebook] return facebook

class Solution:
    def findWord(self, Dict):
        self._dict = Dict
        self._dict.sort(cmp = lambda x, y: cmp(len(x), len(y)))
        i = len(self._dict) - 1
        while i >= 0:
            cur = self._dict.pop()
            if self.wordbreak(cur):
                return cur
            i -= 1
        return -1
    
    def wordbreak(self, word):
        dp = [True] + [False] * len(word)
        for i in range(1, len(dp)):
            for w in self._dict:
                if i >= len(w) and word[i-len(w):i] == w and dp[i-len(w)]:
                    dp[i] = True
        return dp[len(word)]

if __name__ == "__main__":
    solu = Solution()
    A = ["face", "fa", "ce", "boo", "k", "facebook"]
    B = []
    C = ["face", "fa", "ce", "boo", "k", "facebok"]
    D = ["face", "book"]
    print solu.findWord(A)