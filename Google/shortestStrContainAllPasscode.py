class Solution:
    def shortestStrContainAllPasscode(self, level):
        if level <= 0: return ''
        if level == 1: return '0123456789'
        passcodePool = self.generatePool(level)
        startCode = passcodePool.pop(0)
        passcodePool = set(passcodePool)
        self.res = []
        self.level = level
        self.helper(passcodePool, startCode)
        return self.res

    def helper(self, passcodePool, path):
        print path
        if len(passcodePool) == 0:
            self.res.append(path)
            return
        for digit in '0123456789':
            temp = path + digit
            if temp[-self.level:] in passcodePool:
                passcodePool.remove(temp[-self.level:])
                self.helper(passcodePool, temp)
                passcodePool.add(temp[-self.level:])


    def generatePool(self, level):
        if level == 1: return ['0','1','2','3','4','5','6','7','8','9']
        res = []
        for s in '0123456789':
            remain = self.generatePool(level-1)
            for digit in remain:
                res.append(s+digit)
        return res

solution = Solution()
print solution.shortestStrContainAllPasscode(2)
