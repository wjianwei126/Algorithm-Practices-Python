class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: List[List[int]]
        """
        if not beginWord or not endWord or not wordList: return []
        if len(beginWord) != len(endWord): return []

        set1, set2 = set(), set()
        set1.add(beginWord)
        set2.add(endWord)
        self.dic = wordList
        self.reMap = {}
        res = []

        self.helper(set1, set2, True)

        stack = [(beginWord, [beginWord])]
        while stack:
            word, path = stack.pop()
            if word == endWord:
                res.append(path)
            else:
                if word not in self.reMap:
                    continue
                else:
                    for w in self.reMap[word]:
                        stack.append((w, path + [w]))

        return res

    def helper(self, set1, set2, direction):
        if not set1:
            return
        if len(set1) > len(set2):
            direction = not direction
            return self.helper(set2, set1, direction)

        for w in set1:
            if w in self.dic:
                self.dic.remove(w)
        for w in set2:
            if w in self.dic:
                self.dic.remove(w)

        newSet = set()
        done = False

        for word in set1:
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if c != word[i]:
                        newWord = word[:i] + c + word[i+1:]

                        key = word if direction else newWord
                        value = newWord if direction else word

                        if newWord in set2:
                            done = True
                            if key in self.reMap:
                                self.reMap[key].append(value)
                            else:
                                self.reMap[key] = [value]

                        if not done and newWord in self.dic:
                            newSet.add(newWord)
                            if key in self.reMap:
                                self.reMap[key].append(value)
                            else:
                                self.reMap[key] = [value]

        if done:
            return
        else:
            direction = not direction
            return self.helper(set2, newSet, direction)

if __name__ == '__main__':
    solu = Solution()
    beginWord = 'hot'
    endWord = 'dog'
    wordList = ["hot","cog","dog","tot","hog","hop","pot","dot"]
    print solu.findLadders(beginWord, endWord, wordList)
