class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        if not words: return [' ' * maxWidth]
        i = 0
        line = ''
        res = []
        while i < len(words):
            print i
            if line == '':
                tempLine = words[i]
            else:
                tempLine = line + ' ' + words[i]

            if len(tempLine) == maxWidth:
                res.append(tempLine)
                line = ''
                i += 1
            elif len(tempLine) < maxWidth:
                line = tempLine
                i += 1
            else:
                lineWords = line.split(' ')
                length = 0
                for w in lineWords:
                    length += len(w)
                spaceNum = maxWidth - length
                interNum = len(lineWords) - 1
                if interNum == 0:
                    line = line + ' ' * (maxWidth - len(line))
                else:
                    spaces = [0] * interNum
                    for j in range(spaceNum):
                        spaces[j%interNum] += 1
                    line = lineWords[0]
                    for j in range(1, len(lineWords)):
                        line = line + ' '*spaces[j-1] + lineWords[j]
                res.append(line)
                line = ''
        line = line + ' ' * (maxWidth - len(line))
        res.append(line)
        return res

if __name__ == '__main__':
    solu = Solution()
    words = ["Listen","to","many,","speak","to","a","few."]
    maxWidth = 6
    print solu.fullJustify(words, maxWidth)
