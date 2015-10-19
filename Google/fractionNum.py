class Fraction:
    def __init__(self, num, deno):
        if deno == 0:
            raise ValueError('The denominator can not be zero')
        if num > 0 and deno < 0 or num < 0 and deno > 0:
            self.sign = -1
        elif num == 0:
            self.sign = 0
        else:
            self.sign = 1
        self.num = abs(num)
        self.deno = abs(deno)

    def equals(self, fraction):
        if self.sign != fraction.sign:
            return False
        if self.sign == 0 and fraction.sign == 0:
            return True

        gcd1 = self.GCD(self.num, self.deno)
        gcd2 = self.GCD(fraction.num, fraction.deno)
        num1 = self.num/gcd1
        num2 = fraction.num/gcd2
        deno1 = self.deno/gcd1
        deno2 = fraction.deno/gcd2
        return num1 == num2 and deno1 == deno2

    def GCD(self, num1, num2):
        if num1 == num2: return num1
        return self.GCD(num1-num2, num2) if num1 > num2 else self.GCD(num1, num2-num1)

f1 = Fraction(1, 0)
f2 = Fraction(2, -3)
print f1.equals(f2)
