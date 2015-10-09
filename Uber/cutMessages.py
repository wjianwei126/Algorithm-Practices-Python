class Solution:
    def cutMessage(self, message, length):
        if not message: return []
        if length <= 5 : return []
        estimatedNumber = len(message) / (length - 7)
        if estimatedNumber < 10:
            mark = 5
            curMarkLen = 5
        elif estimatedNumber >= 10 and estimatedNumber < 100:
            mark = 7
            curMarkLen = 6
        else:
            mark = 9
            curMarkLen = 7

        words = message.split(' ')
        i = 0
        curLine = ''
        res = []
        count = 0
        reachTens = False
        reachHundreds = False
        while i < len(words):
            if len(words[i]) > length - curMarkLen:
                raise Exception('Word too long in the message - ' + words[i])

            if curLine == '':
                temp = words[i]
            else:
                temp = curLine + ' ' + words[i]

            if len(temp) > length - curMarkLen:
                count += 1
                curLine += '(' + str(count)
                res.append(curLine)
                curLine = ''
                if count >= 10 and not reachTens:
                    curMarkLen += 1
                    reachTens = True
                if count >= 100 and not reachHundreds:
                    curMarkLen += 1
                    reachHundreds = True
                continue

            curLine = temp
            i += 1

        count += 1
        curLine += '(' + str(count)
        res.append(curLine)

        for i in range(len(res)):
            res[i] += '/' + str(count) + ')'

        return res

solution = Solution()
message = 'I am a second year Master student from Columbia University. I am a second year Master student from Columbia University. I am a second year Master student from Columbia University.'
res = solution.cutMessage(message, 30)
print res
maxlen = 0
for message in res:
    maxlen = max(maxlen, len(message))
print maxlen
