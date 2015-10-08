class Solution(object):
    dic = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], \
    '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], \
    '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
    def letterCombination(self, digits):
        if not digits: return []
        for num in digits:
            if num not in '23456789': return []
        return self.helper(digits)

    def helper(self, digits):
        if not digits: return []
        if len(digits) == 1: return self.dic[digits[0]]

        res = []
        remain = self.helper(digits[1:])
        for letter in self.dic[digits[0]]:
            for combination in remain:
                res.append(letter+combination)
        return res

    def letterCombinationIterative(self, digits):
        if not digits: return []
        for num in digits:
            if num not in '23456789': return []
        if len(digits) == 1: return self.dic[digits[0]]

        stack = []
        firstLetter = self.dic[digits[0]]
        for letter in firstLetter:
            stack.append((letter, 0))

        res = []
        while stack:
            combination, index = stack.pop()
            if index == len(digits) - 1:
                res.append(combination)
                continue
            nextLetter = self.dic[digits[index+1]]
            for letter in nextLetter:
                stack.append((combination+letter, index+1))
        return res



solution = Solution()
digits = '28'
print solution.letterCombination(digits)
print solution.letterCombinationIterative(digits)
