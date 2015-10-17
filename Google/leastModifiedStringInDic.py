class Solution:
    def leastModifiedStringInDic(self, dic, s):
        self.dic = dic
        self.res = ''
        self.helper(s)
        return self.res

    def helper(self, targetStr):
        if targetStr in self.dic:
            if len(targetStr) > len(self.res):
                self.res = targetStr
                return
        for i in range(len(targetStr)):
            newString = targetStr[:i] + targetStr[i+1:]
            self.helper(newString)

solution = Solution()
dic = set(['abc', 'abd', 'acde', 'abde', 'abdea'])
s = 'abdee'
print solution.leastModifiedStringInDic(dic, s)
