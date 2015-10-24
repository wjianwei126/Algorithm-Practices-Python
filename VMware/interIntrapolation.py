import math
def  Interpolate( n,  amount,  ucost):
    if len(ucost) == 1: return ucost[0]
    for i in xrange(len(amount)):
        amount[i] = int(amount[i])
    for j in xrange(len(ucost)):
        ucost[j] = float(ucost[j])
    count = 0
    for i in xrange(len(ucost)):
        if ucost[i] > 0:
            mark = i
            count += 1
    if count == 1: return ucost[mark]

    left = 0
    right = len(amount) - 1
    while left <= right:
        mid = left + (right - left) / 2
        if amount[mid] == n:
            return ucost[mid]
        elif amount[mid] > n:
            right = mid - 1
        else:
            left = mid + 1
    if right == -1:
        p1 = p2 = None
        for i in xrange(len(ucost)):
            if ucost[i] > 0:
                if not p1:
                    p1 = i
                elif not p2:
                    p2 = i
                    break
        return polation(amount[p1], amount[p2], ucost[p1], ucost[p2], n)
    elif left == len(amount):
        p1 = p2 = None
        for i in xrange(len(ucost)-1, -1, -1):
            if ucost[i] > 0:
                if not p2:
                    p2 = i
                elif not p1:
                    p1 = i
                    break
        return polation(amount[p1], amount[p2], ucost[p1], ucost[p2], n)
    else:
        p1, p2 = right, left
        while p1 >= 0 and ucost[p1] <= 0:
            p1 -= 1
        while p2 < len(ucost) and ucost[p2] <= 0:
            p2 += 1
        if p1 == -1:
            p1 = p2
            p2 += 1
            while ucost[p2] <= 0:
                p2 += 1
        elif p2 == len(ucost):
            p2 = p1
            p1 -= 1
            while ucost[p1] <= 0:
                p1 -= 1
        return polation(amount[p1], amount[p2], ucost[p1], ucost[p2], n)

def polation(x, y, fx, fy, k):
    print x, y, fx, fy, k
    return math.ceil(((fy - fx) * (k - x) / (y - x) + fx)*100)/100
    return

n = 2000
amount = ['10', '25', '50', '100', '500']
ucost = ['27.32', '23.13', '21.25', '18.00', '15.50']
print Interpolate(n, amount, ucost)
