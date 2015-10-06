# Given a list of words, find two words with no sharing characters that reach the maximum length product
class Solution:
    def maxLenProduct(self, words):
        if not words: return 0
        dic = {}
        # O(n*k)
        for word in words:
            for c in word:
                if c in dic:
                    dic[c].add(word)
                else:
                    dic[c] = set([word])

        res = 0
        for word in words: # O(n)
            shared = set()
            for c in word: # O(k)
                shared |= dic[c]
            for w in words: # O(n)
                if w not in shared:
                    res = max(res, len(word) * len(w))

        return res

solu = Solution()
words = ['cat', 'dog', 'feed', 'pull', 'spacee']
print solu.maxLenProduct(words)
