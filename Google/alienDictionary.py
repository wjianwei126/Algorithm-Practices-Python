# There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of words from the dictionary, wherewords are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.
#
# For example,
# Given the following words in dictionary,
#
# [
#   "wrt",
#   "wrf",
#   "er",
#   "ett",
#   "rftt"
# ]
# The correct order is: "wertf".
#
# Note:
#
# You may assume all letters are in lowercase.
# If the order is invalid, return an empty string.
# There may be multiple valid order of letters, return any one of them is fine.
class Node(object):
    def __init__(self):
        self.IN = set()
        self.OUT = set()

class Solution(object):
    def alienOrder(self, words):
        # find out nodes
        graph = {}
        for word in words:
            for letter in word:
                if letter not in graph:
                    graph[letter] = Node()

        # find out directed edges (from StefanPochmann)
        for pair in zip(words, words[1:]):
            for a, b in zip(*pair):
                if a != b:
                    graph[a].OUT.add(b)
                    graph[b].IN.add(a)
                    break

        # topo-sort
        res = ""
        while graph:
            oldlen = len(graph)

            for key in graph:
                if not graph[key].IN:   # to remove this
                    for key2 in graph[key].OUT:
                        graph[key2].IN.remove(key)
                    del graph[key]
                    res += key
                    break

            if oldlen == len(graph): # if shrinking stops, solution doesn't exist
                return ""
            oldlen = len(graph)
        return res

words = ['wrt', 'wrf', 'er', 'ett', 'rftt']
solution = Solution()
print solution.alienOrder(words)
