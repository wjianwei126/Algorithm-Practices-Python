class Solution:
    def findLongestChain(self, words):
        if not words: return 0
        dic = {}
        longestWL = 0
        for w in words:
            wordLen = len(w)
            longestWL = max(longestWL, wordLen)
            if wordLen in dic:
                dic[wordLen].add(w)
            else:
                dic[wordLen] = set([w])
        print dic
        print longestWL

        queue = []

        for string in dic[longestWL]:
            queue.append((string, longestWL, 1))

        maxChainLen = 0

        while queue:
            word, wordLen, chainLen = queue.pop(0)
            if wordLen == 1:
                maxChainLen = max(maxChainLen, chainLen)
                continue
            noNext = True
            if wordLen-1 in dic:
                for i in xrange(wordLen):
                    newWord = word[:i] + word[i+1:]
                    if newWord in dic[wordLen-1]:
                        queue.append((newWord, wordLen-1, chainLen+1))
                        noNext = False
            if noNext:
                maxChainLen = max(maxChainLen, chainLen)

        return maxChainLen

    def findLongestChain2(self, words):
        dic = set()
        for w in words:
            dic.add(w)
        res = 0

        myMap = {}
        for i in xrange(len(words)):
            length = self.helper(words[i], dic, myMap) + 1
            myMap[words[i]] = length
            res = max(res, length)

        return res

    def helper(self, word, dict, myMap):
        for i in xrange(len(word)):
            newWord = word[:i] +  word[i+1:]
            if newWord in dict:
                if newWord in myMap:
                    return myMap[newWord]
                return self.helper(newWord, dict, myMap) + 1
        return 0

if __name__ == '__main__':
    solu = Solution()
    words = ['a', 'cd', 'c', 'bcd', 'abcd', 'abd']
    # words = ['bcd', 'abcd', 'abd']
    print solu.findLongestChain2(words)
