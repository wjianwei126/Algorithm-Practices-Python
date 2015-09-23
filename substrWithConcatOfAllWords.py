class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words: return []
        dic = {}
        for word in words:
            dic[word] = dic.get(word, 0) + 1

        wordLen = len(words[0])
        wordNum = len(words)
        totalLen = wordLen * wordNum
        if totalLen > len(s):
            return []

        i = 0
        res = []
        while i <= len(s) - totalLen:
            bgn = i
            end = i + totalLen
            j = i
            used = {}
            while j < end:
                temp = s[j:j+wordLen]
                if temp not in dic:
                    break
                used[temp] = used.get(temp, 0) + 1
                if used[temp] > dic[temp]:
                    break
                j += wordLen
            if j == end:
                res.append(i)
            i += 1
        return res

if __name__ == '__main__':
    solu = Solution()
    s = "barfoothefoobarman"
    words = ['foo', 'bar']
    print solu.findSubstring(s, words)
