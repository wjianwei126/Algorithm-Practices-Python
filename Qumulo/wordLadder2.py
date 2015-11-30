class Solution:
    def wordLadder2(self, beginWord, endWord, wordList):
        self.path = None
        self.endWord = endWord
        self.helper(beginWord, wordList, [beginWord])
        return self.path

    def helper(self, beginWord, wordList, curPath):
        if self.path:
            return

        for i in range(len(beginWord)):
            for j in 'abcdefghijklmnopqrstuvwxyz':
                if beginWord[i] == j:
                    continue
                newWord = beginWord[:i] + j + beginWord[i+1:]
                if newWord == self.endWord:
                    self.path = curPath + [newWord]
                    return
                if newWord in wordList:
                    wordList.remove(newWord)
                    self.helper(newWord, wordList, curPath + [newWord])
                    wordList.add(newWord)

solution = Solution()
beginWord = 'snap'
endWord = 'chat'
wordList = set(['snat', 'shat', 'shap', 'chap', 'snag'])
print solution.wordLadder2(beginWord, endWord, wordList)
