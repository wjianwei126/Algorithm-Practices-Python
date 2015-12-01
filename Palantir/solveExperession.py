# Find out a map from char to number that meets the patter
# ONE
# +ONE
# ----
# TWO
#
# 231
# +231
# ----
# 462
#
# return {O:2, N:3, E:1, T:4, W:6}
#
# FOUR
# +FOUR
# -----
# EIGHT
#
# 5239
# +5239
# -----
# 10478
#
# FOUR
# +ONE
# ----
# FIVE
#
# 6130
# +149
# ----
# 6279

class EvalExpression:
    def findMap(self, s1, s2, result):
        self.s1, self.s2, self.result = s1, s2, result
        charSet = set()
        for ch in s1+s2+result:
            charSet.add(ch)

        self.charList = []
        for ch in charSet:
            self.charList.append(ch)

        solution = {}
        numberVisited = set()
        if self.dfs(solution, numberVisited, 0):
            return solution
        return None

    def dfs(self, solution, numberVisited, pos):
        if pos == len(self.charList):
            return self.evaluate(solution)

        for num in range(10):
            if num in numberVisited:
                continue
            numberVisited.add(num)
            solution[self.charList[pos]] = num
            if self.dfs(solution, numberVisited, pos+1):
                return True
            numberVisited.remove(num)
        return False

    def evaluate(self, solution):
        num1 = 0
        for ch in self.s1:
            num1 = num1 * 10 + solution[ch]
        num2 = 0
        for ch in self.s2:
            num2 = num2 * 10 + solution[ch]
        res = 0
        for ch in self.result:
            res = res * 10 + solution[ch]
        return num1 + num2 == res

exeval = EvalExpression()
print exeval.findMap('ONE', 'ONE', 'TWO')
print exeval.findMap('FOUR', 'FOUR', 'EIGHT')
print exeval.findMap('FOUR', 'ONE', 'FIVE')
