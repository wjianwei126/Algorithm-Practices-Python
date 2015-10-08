class Solution(object):
    def wordBreak(self, s, words):
        if not words or not s: return False
        dp = [True] + [False] * len(s)
        for i in range(1, len(s)+1):
            for word in words:
                if i >= len(word) and s[i-len(word):i] == word and dp[i-len(word)]:
                    dp[i] = True
        return dp[len(s)]

solution = Solution()
s = 'helloworld'
words = ['hello', 'world', 'hell', 'oworld']
s = ''
words = []
print solution.wordBreak(s, words)
