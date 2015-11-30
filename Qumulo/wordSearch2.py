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

    def find(self, word):
        node = self.root
        for w in word:
            if w not in node.children:
                return False
            node = node.children[w]
        return node.end

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not words: return []
        trie = Trie()
        for word in words:
            trie.insert(word)
        self.res = []
        self.visited = set()

        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, trie.root, i, j, '')
        return self.res

    def dfs(self, board, node, i, j, path):
        if node.end:
            self.res.append(path)
            node.end = False
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or (i, j) in self.visited:
            return

        ch = board[i][j]
        print ch
        if ch not in node.children:
            return

        newNode = node.children[ch]
        self.visited.add((i, j))
        self.dfs(board, newNode, i+1, j, path+ch)
        self.dfs(board, newNode, i-1, j, path+ch)
        self.dfs(board, newNode, i, j+1, path+ch)
        self.dfs(board, newNode, i, j-1, path+ch)
        self.visited.remove((i, j))

board = ["oaan","etae","ihkr","iflv"]
words = ["oath","pea","eat","rain"]
board = ['a']
words = ['a']
solution = Solution()
print solution.findWords(board, words)
