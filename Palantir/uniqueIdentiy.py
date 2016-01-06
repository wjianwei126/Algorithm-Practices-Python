class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.end = True

    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children
        return node.end

    def searchIdentify(self, word):
        node = self.root
        res = ''
        for ch in word:
            res += ch
            # print res, node.children[ch].end
            if len(node.children[ch].children.keys()) > 1 or node.children[ch].end:
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
