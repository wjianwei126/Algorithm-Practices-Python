class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if not tokens:
            return 0
        stack = []
        for token in tokens:
            if token in '+-*/':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(self.calc(num1, num2, token))
            else:
                stack.append(int(token))
        return stack[0]

    def calc(self, num1, num2, op):
        if op == '+':
            return num1+num2
        elif op == '-':
            return num1-num2
        elif op == '*':
            return num1*num2
        else:
            if num2 == 0:
                raise ValueError('devisor can not be 0')
            if num1 * num2 < 0:
                return - (abs(num1) / abs(num2))
            else:
                return num1 / num2

solu = Solution()
solu.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])


from abc import abstractmethod
class Token(object):
    @abstractmethod
    def isValue(self):
        pass

    @abstractmethod
    def execute(self, stack):
        pass

class Operand(Token):
    def __init__(self, value=None):
        self.value = value

    def isValue(self):
        return True

    def getValue(self):
        return self.value

    def setValue(self, x):
        self.value = x

    def execute(self, stack):
        stack.append(self.value)

class Operator(Token):
    def __init__(self, mark=None, cal=None):
        self.mark = mark
        self.cal = cal

    def isValue(self):
        return False

    def getOperation(self):
        return self.mark

    def execute(self, stack):
        try:
            num2 = stack.pop()
            num1 = stack.pop()
        except:
            print 'Invalid notation!'
            raise

        res = self.cal(num1, num2)
        stack.append(res)

class OperationFactory(object):
    def __init__(self):
        self.map = {}
        self.map['+'] = lambda x, y: x+y
        self.map['-'] = lambda x, y: x-y
        self.map['*'] = lambda x, y: x*y
        self.map['/'] = lambda x, y: x/y if x*y>0 else -(abs(x)/abs(y))

    def create(self, s):
        if s not in self.map:
            return Operand(int(s))
        else:
            return Operator(s, self.map[s])

if __name__ == "__main__":
    inputList = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    # inputList = ['10', '3', '+', '7', '-']
    factory = OperationFactory()
    stack = []
    for i in inputList:
        token = factory.create(i)
        token.execute(stack)

    print stack
