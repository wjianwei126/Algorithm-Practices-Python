def findCommon(l1, l2):
    if not l1 or not l2: return []
    p1 = p2 = 0
    res = []
    while p1 < len(l1) and p2 < len(l2):
        if l1[p1] == l2[p2]:
            if not res or res and res[-1] != l1[p1]:
                res.append(l1[p1])
            p1 += 1
            p2 += 1
        else:
            if l1[p1] < l2[p2]:
                p1 += 1
            else:
                p2 += 1
    return res

l1 = [1,2,3,7,8,10]
l2 = [3,5,6,7,9,10,11]
l1 = [1,1,1,7,8,10]
l2 = [1,5,6,7,9,10,11]
l1 = [1,1,1,7,8,10]
l2 = [2,5,6,9,11]
print findCommon(l1, l2)
