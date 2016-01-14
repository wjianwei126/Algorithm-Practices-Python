# Given a string and two words
# return the substring where the two words are the closest to each other (including the former and later 3 words)
# e.g. Indeed use python and java to deal with the python python and is for java
# words: python, java
# return  Indeed use python and java to deal with

def findShortestDistance(sentence, word1, word2):
    if not sentence: return -1
    wordList = sentence.split(' ')
    p1 = p2 = -1
    optimalP1 = optimalP2 = -1
    shortest = float('inf')
    for i in range(len(wordList)):
        if wordList[i] == word1:
            p1 = i
        elif wordList[i] == word2:
            p2 = i
        if p1 != -1 and p2 != -1 and abs(p1-p2) < shortest:
            shortest = abs(p1-p2)
            optimalP1 = p1
            optimalP2 = p2

    return ' '.join(wordList[optimalP1:optimalP2+1]) if optimalP1 < optimalP2 else ' '.join(wordList[optimalP2:optimalP1+1])

sentence = 'Indeed use python and java to deal with the python python and is for java'
print findShortestDistance(sentence, 'python', 'java')
print findShortestDistance(sentence, 'java', 'python')

# If this method will be called several times
class Shortest:
    def __init__(self, sentence):
        wordList = sentence.split(' ')
        self.wordDic = {}
        for i in range(len(wordList)):
            if wordList[i] not in self.wordDic:
                self.wordDic[wordList[i]] = []
            self.wordDic[wordList[i]].append(i)
        self.wordList = wordList

    def findShortestDistance(self, word1, word2):
        indices1 = self.wordDic[word1]
        indices2 = self.wordDic[word2]
        optimalP1 = optimalP2 = -1
        p1 = p2 = 0
        shortest = float('inf')
        while p1 < len(indices1) and p2 < len(indices2):
            if abs(indices1[p1] - indices2[p2]) < shortest:
                shortest = abs(indices1[p1] - indices2[p2])
                optimalP1 = indices1[p1]
                optimalP2 = indices2[p2]
            if indices1[p1] < indices2[p2]:
                p1 += 1
            else:
                p2 += 1

        return ' '.join(self.wordList[optimalP1:optimalP2+1]) if optimalP1 < optimalP2 else ' '.join(self.wordList[optimalP2:optimalP1+1])

myClass = Shortest(sentence)
print myClass.findShortestDistance('python', 'java')
print myClass.findShortestDistance('java', 'python')
