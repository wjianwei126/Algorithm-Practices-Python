class Solution:
    def letterCombinations(self, pattern):
        if not pattern: return []
        i = 0
        temp = ''
        res = []
        while i < len(pattern):
            if not self.isLetter(pattern[i]):
                temp += pattern[i]
                i += 1
            else:
                break

        if i == len(pattern):
            return [temp]

        remain = self.letterCombinations(pattern[i+1:])
        for combi in remain:
            res.append(temp + pattern[i] + combi)
            res.append(temp + self.switch(pattern[i]) + combi)

        return res

    def isLetter(self, ch):
        if ord(ch) >= ord('a') and ord(ch) <= ord('z') or \
            ord(ch) >= ord('A') and ord(ch) <= ord('Z'):
            return True
        else:
            return False

    def switch(self, ch):
        if ord(ch) >= ord('a') and ord(ch) <= ord('z'):
            return chr(ord(ch) + ord('A') - ord('a'))
        else:
            return chr(ord(ch) + ord('a') - ord('A'))

solu = Solution()
print solu.letterCombinations('ab7d82')
