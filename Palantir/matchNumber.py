# A000000-A999999
def matchNumber(num):
    divisor = 100000
    preZeroCount = 0
    while divisor > num:
        divisor /= 10
        preZeroCount += 1

    prefix = 'A' + preZeroCount * '0'

    res = []
    count = 0
    countRound = 1
    noStar = False
    while divisor > 0:
        if divisor == 1:
            noStar = True
        digit = num / divisor
        starDigitsNum = log(10, divisor)
        if countRound == 1:
            for i in range(digit):
                match = prefix + str(i)
                match += '*' if not noStar else ''
                res.append(match)
        else:
            prefix += str(count)
            for i in range(digit):
                match = prefix + str(i)
                match += '*' if not noStar else ''
                res.append(match)
        countRound += 1
        count = digit
        num -= digit * divisor
        divisor /= 10
    print res

def log(base, num):
    count = 0
    while num > 1:
        num /= base
        count += 1
    return count

matchNumber(20375)
