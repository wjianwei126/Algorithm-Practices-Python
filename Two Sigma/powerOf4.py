def powerOfFour1(num):
    # O(logN)
    if num <= 0: return False
    while num % 4 == 0:
        num /= 4
    return num == 1

def powerOfFour2(num):
    # O(64)
    # 1   0 0000 0001
    # 4   0 0000 0100
    # 16  0 0001 0000
    # 64  0 0100 0000
    # 256 1 0000 0000
    # Check for odd digits
    res = False
    if num <= 0: return False
    for i in range(1, 64):
        if num & 1 == 1:
            if i % 2 == 0:
                return False
            else:
                if res:
                    return False
                else:
                    res = True
        num >>= 1
    return res

def powerOfFour3(num):
    # O(3)
    # 1. check greater than zero
    # 2. check only one digit 1 in the number (power of two)
    # 3. check digit 1 at odd digit
    return num > 0 and num & (num - 1) == 0 and num & 0x5555555555555555L == num

for num in [-5, 0, 1, 2, 4, 5, 16, 32, 2**62, 2**63-1]:
    print powerOfFour1(num), powerOfFour2(num), powerOfFour3(num)
