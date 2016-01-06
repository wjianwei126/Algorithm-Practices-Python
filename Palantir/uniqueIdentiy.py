class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.count += 1
        node.end = True

    def searchIdentify(self, word):
        node = self.root
        res = ''
        for ch in word:
            res += ch
            if node.children[ch].count > 1:
                node = node.children[ch]
            else:
                break
        return res

def uniqueIdentify(words):
    myTrie = Trie()
    for word in words:
        myTrie.insert(word)
    res = []
    for word in words:
        res.append(myTrie.searchIdentify(word))
    return res

words = ['ab', 'ad', 'abcde', 'xyz']
words = ['cde', 'cdefghi', 'cfh']
print uniqueIdentify(words)
