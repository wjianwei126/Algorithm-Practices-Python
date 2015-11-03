class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
            node = node.children[w]
        node.end = True

    def find(self, word, node = None):
        if not word: return False
        if not node:
            node = self.root
        for w in word:
            if w not in node.children:
                return False
            node = node.children[w]
        return node.end

    def findOneTypo(self, word):
        node = self.root
        prevNode = None
        i = 0
        while i < len(word):
            if word[i] in node.children:
                prevNode = node
                node = node.children[word[i]]
                i += 1
                continue

            if i == len(word) - 1:
                return True

            for child in node.children:
                if self.find(word[i+1:], node.children[child]):
                    return True
            if prevNode:
                curNode = self.root
                j = 0
                while j < i:
                    for child in curNode.children:
                        if self.find(word[j+1:], curNode.children[child]):
                            return True
                    curNode = curNode.children[word[j]]
                    j += 1
                for child in prevNode.children:
                    if self.find(word[i:], prevNode.children[child]):
                        return True
            return False
        return False

    def findOneTypo2(self, word):
        # O(26*wordlength*wordlength)
        if self.find(word): return False
        for i in range(len(word)):
            for j in 'abcdefghijklmnopqrstuvwxyz':
                if j == word[i]: continue
                newWord = word[:i] + j + word[i+1:]
                if self.find(newWord): return True
        return False

class Solution:
    def onlyOneTypo(self, wordDict, word):
        trieDict = Trie()
        for dicWord in wordDict:
            trieDict.insert(dicWord)
        return trieDict.findOneTypo(word), trieDict.findOneTypo2(word)

solution = Solution()
wordDict = ['google', 'gooktx', 'giokpl', 'giable']
print solution.onlyOneTypo(wordDict, 'goabke')
