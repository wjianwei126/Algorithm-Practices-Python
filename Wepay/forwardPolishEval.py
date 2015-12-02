#  input (+ (* 2 3) (/ (+ 4 5) 3)) returns 9
def evalExpression(s):
    if not s: return None
    stack = []
    num = 0
    calNum = False
    for ch in s:
        if ch.isdigit():
            num = num * 10 + int(ch)
            calNum = True
        elif ch == ' ':
            if calNum:
                stack.append(num)
                num = 0
                calNum = False
        elif ch == ')':
            if calNum:
                stack.append(num)
                num = 0
                calNum = False
            num2 = int(stack.pop())
            num1 = int(stack.pop())
            op = stack.pop()
            stack.pop()
            res = calculate(num1, num2, op)
            stack.append(res)
        else:
            stack.append(ch)
    return stack[0]


def calculate(num1, num2, op):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    else:
        return num1 / num2

s = '(+ (* 2 3) (/ (+ 4 5) 3))'
print evalExpression(s)
