class BigInt:
    def __init__(self, s):
        self.positive = True
        if not s:
            self.string = ''
        elif s[0] == '+':
            self.string = s[1:]
        elif s[0] == '-':
            self.positive = False
            self.string = s[1:]
        else:
            self.string = s
class Solution:
    def add(self, bigInt1, bigInt2):
        if bigInt1.positive and bigInt2.positive:
            p1 = len(bigInt1.string) - 1
            p2 = len(bigInt2.string) - 1
            carry = 0
            res = ''
            while p1 >= 0 or p2 >= 0:
                num1 = int(bigInt1.string[p1]) if p1 >= 0 else 0
                num2 = int(bigInt2.string[p2]) if p2 >= 0 else 0
                tempSum = num1 + num2 + carry
                res = str(tempSum % 10) + res
                carry = tempSum / 10
                p1 -= 1
                p2 -= 1
            if carry > 0:
                res = str(carry) + res
            return res
        elif bigInt1.positive and not bigInt2.positive:
            return self.subtract(bigInt1, BigInt(bigInt2.string))
        elif not bigInt1.positive and bigInt2.positive:
            return self.subtract(bigInt2, BigInt(bigInt1.string))
        else:
            return '-' + self.add(BigInt(bigInt1.string), BigInt(bigInt2.string))

    def subtract(self, bigInt1, bigInt2):
        if not bigInt1.positive and not bigInt2.positive:
            return self.subtract(BigInt(bigInt2.string), BigInt(bigInt1.string))
        elif bigInt1.positive and not bigInt2.positive:
            return self.add(bigInt1, BigInt(bigInt2.string))
        elif not bigInt1.positive and bigInt2.positive:
            return '-' + self.add(BigInt(bigInt1.string), bigInt2)
        else:
            s1 = bigInt1.string
            s2 = bigInt2.string
            isMinus = False
            if self.compareABS(bigInt1.string, bigInt2.string) < 0:
                s1, s2 = s2, s1
                isMinus = True
            p1 = len(s1) - 1
            p2 = len(s2) - 1
            borrow = 0
            res = ''
            while p1 >= 0 or p2 >= 0:
                num1 = int(s1[p1]) if p1 >= 0 else 0
                num2 = int(s2[p2]) if p2 >= 0 else 0
                tempDiff = - borrow + num1 - num2
                if tempDiff < 0:
                    remain = 10 + tempDiff
                    borrow = 1
                else:
                    remain = tempDiff
                    borrow = 0
                res = str(remain) + res
                p1 -= 1
                p2 -= 1
            return res if not isMinus else '-' + res

    def compareABS(self, s1, s2):
        if len(s1) > len(s2):
            return 1
        elif len(s1) < len(s2):
            return -1
        else:
            for i in range(len(s1)):
                if int(s1[i]) > int(s2[i]):
                    return 1
                elif int(s1[i]) < int(s2[i]):
                    return -1
            return 0
solution = Solution()
A = BigInt('234')
B = BigInt('923')
A = BigInt('234')
B = BigInt('-923')
A = BigInt('-234')
B = BigInt('923')
A = BigInt('-234')
B = BigInt('-923')
print solution.add(A, B)
print solution.subtract(A, B)
