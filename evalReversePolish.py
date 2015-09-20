class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if not tokens or len(tokens) == 0: return
        stack = []
        for i in range(len(tokens)):
            if tokens[i] in "+-*/":
                n2 = stack.pop()
                n1 = stack.pop()
                res = self.operate(n1, n2, tokens[i])
                stack.append(res)
            else:
                stack.append(int(tokens[i]))
            print stack
        return stack[-1]

    def operate(self, n1, n2, op):
        if op == '+':
            return n1 + n2
        elif op == '-':
            return n1 - n2
        elif op == '*':
            return n1 * n2
        else:
            return n1 / n2

if __name__ == '__main__':
    solu = Solution()
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print solu.evalRPN(tokens)
