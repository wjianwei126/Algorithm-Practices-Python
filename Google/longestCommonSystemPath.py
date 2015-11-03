# 白人老太太，9年码工，题目是给一堆系统路径，类似“/abc/xyz/hij/f1”，找最长公共路径。.
# 我说了longest common prefix的，她说怎么优化，于是说字典树，又问是不是要建完整的一颗树，
# 于是说不用，发现要分叉了就标记一下跳出，然后从根节点找到高度最低的分叉点就是公共路径
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        self.childrenNum = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, words):
        node = self.root
        for w in words:
            if w not in node.children:
                node.children[w] = TrieNode()
                node.childrenNum += 1
            node = node.children[w]
        node.end = True

    def findLongestCommon(self):
        node = self.root
        res = '/'
        while node.childrenNum == 1:
            child = node.children.keys()[0]
            res += child + '/'
            node = node.children[child]
        return res

    # without adding all the paths
    def add2(self, words):
        node = self.root
        # first path
        if node.childrenNum == 0:
            for w in words:
                if w not in node.children:
                    node.children[w] = TrieNode()
                    node.childrenNum += 1
                node = node.children[w]
            node.end = True
        # other paths
        else:
            for w in words:
                if w not in node.children:
                    node.end = True
                    break
                else:
                    node = node.children[w]
            node.end = True

    def findLongestCommon2(self):
        node = self.root
        res = '/'
        while not node.end:
            child = node.children.keys()[0]
            res += child + '/'
            node = node.children[child]
        return res

paths = ['/abc/xyz/hij/f1', '/abc/xyz/hij/f1/aaa', '/abc/xyz/bky', '/abc/xyz/bky/f1']
paths = ['/abc/bcd', '/cd/bcd']
trie = Trie()
for path in paths:
    thisPath = path[1:].split('/')
    trie.add(thisPath)
print trie.findLongestCommon()
