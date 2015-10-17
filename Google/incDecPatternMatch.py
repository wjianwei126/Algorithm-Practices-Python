class Solution:
    def incDecPatternMatch(self, pattern):
        if not pattern: return ''
        remainNums = set([1,2,3,4,5,6,7,8,9])
        self.res = ''
        for num in remainNums:
            temp = str(num)
            remainNums.remove(num)
            self.helper(remainNums, pattern, num, temp)
            remainNums.add(num)

        return self.res

    def helper(self, remainNums, pattern, formerNum, curString):
        if self.res != '': return
        if not pattern:
            self.res = curString
            return

        if pattern[0] == 'i':
            for num in remainNums:
                if num > formerNum:
                    remainNums.remove(num)
                    self.helper(remainNums, pattern[1:], num, curString + str(num))
                    remainNums.add(num)
        else:
            for num in remainNums:
                if num < formerNum:
                    remainNums.remove(num)
                    self.helper(remainNums, pattern[1:], num, curString + str(num))
                    remainNums.add(num)

solution = Solution()
pattern = 'iiii'
pattern = 'ididid'
pattern = ''
pattern = 'dddddddd'
pattern = 'iiididid'
pattern = 'ddidiii'
print solution.incDecPatternMatch(pattern)
