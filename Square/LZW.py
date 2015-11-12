class LZW:
    def __init__(self, text, dic):
        self.text = text
        self.dic = dic

    def getEncodedText(self):
        i = 0
        encodedText = []
        while i < len(self.text):
            j = i
            while j < len(self.text) and self.text[i:j+1] in self.dic:
                j += 1
            if j == len(self.text):
                encodedText.append(self.dic[self.text[i:j]])
                break
            else:
                encodedText.append(self.dic[self.text[i:j]])
                self.dic[self.text[i:j+1]] = len(self.dic) + 1
                i = j
        return encodedText

    def getDecodedText(self, encodedText):
        revertedDic = {}
        for key in self.dic:
            revertedDic[self.dic[key]] = key

        decodedText = ''
        for num in encodedText:
            decodedText += revertedDic[num]
        return decodedText

text = 'ABAB'
dic = {'A': 1, 'B':2}
text = 'ABCABAC'
dic = {'A': 1, 'B':2, 'C':3}
lzw = LZW(text, dic)
encodedText = lzw.getEncodedText()
print encodedText
print lzw.dic
print lzw.getDecodedText(encodedText)
