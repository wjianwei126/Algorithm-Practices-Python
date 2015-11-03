# 给出一些string，每一个都是一个不包含"/"的路径，比如“usrbinpython”，“usrbinperl”，
# “usrbinjava”，然后要求输出最有可能的路径，比如这个例子就应该输出"usrbin/java",
# "usrbin/p/ython", "usrbin/p/erl". 还有一些follow-up，
# 比如怎样避免这个p被劈开，当输入数据很大的时候，怎样选最有可能的路径之类的。
class TrieNode:
    def __init__(self):
        self.children = {}
        self.childrenNum = 0
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
                node.childrenNum += 1
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

    def printAllPaths(self):
        node = self.root
        self.paths = []
        temp = ''
        self.dfs(node, temp)
        return self.paths

    def dfs(self, node, curPath):
        if node.end:
            self.paths.append(curPath)

        while node and node.childrenNum == 1:
            curPath += node.children.keys()[0]
            node = node.children[node.children.keys()[0]]
            if node.end:
                # if node.childrenNum == 1 and node.end:
                #     curPath += '/'
                self.paths.append(curPath)

        for w in node.children:
            self.dfs(node.children[w], curPath + '/' + w)

class Solution:
    def nonSlashPath(self, paths):
        if not paths: return []
        myTrie = Trie()
        for path in paths:
            myTrie.insert(path)
        return myTrie.printAllPaths()


solution = Solution()
paths = ['usrbinpython', 'usrbinjava', 'usrbinperl']
paths = ['usrbinpython', 'usrbinjava', 'usrbinperl', 'usrsrc', 'usrbinper', 'usr']
print solution.nonSlashPath(paths)
