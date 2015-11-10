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

    def findLongestMatching(self, pre):
        node = self.root
        for w in pre:
            node = node.children[w]
        self.res = []
        self.dfs(node, pre)
        return self.res

    def dfs(self, node, path):
        if node.end:
            self.res.append(path)
        for i in node.children:
            self.dfs(node.children[i], path+i)

trie = Trie()
trie.insert('taxi')
trie.insert('tab')
trie.insert('title')
trie.insert('ta')
print trie.findLongestMatching('ta')
