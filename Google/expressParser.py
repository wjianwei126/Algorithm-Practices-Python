class Solution:
    def expressParser(self, express):
        if not express: return 0
        stack = []
        for i in range(len(express)):
            if express[i] == ')':
                nums = []
                while stack[-1] not in '+*':
                    nums.append(stack.pop())
                op = stack.pop()
                temp = self.calculate(op, nums)
                stack.pop() # pop '('
                stack.append(temp)
            else:
                stack.append(express[i])
        return int(stack[0])

    def calculate(self, op, nums):
        if op == '+':
            res = 0
            for n in nums:
                res += int(n)
        else:
            res = 1
            for n in nums:
                res *= int(n)
        return str(res)

express = '(+12(*34))'
express = '(+123(*123))'
solu = Solution()
print solu.expressParser(express)
