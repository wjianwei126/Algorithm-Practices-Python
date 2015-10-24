def  Circles( distance,  radius,  cost):
    if not cost or not radius: return []
    res = [0] * len(radius)
    curCost = [float('inf')] * len(radius)
    for i in range(len(radius)):
        for j in range(i, len(radius)):
            if radius[i] + radius[j] >= distance:
                thisCost = cost[i] + cost[j]
                if thisCost < curCost[i]:
                    res[i] = j + 1
                    curCost[i] = thisCost
                if thisCost < curCost[j]:
                    res[j] = i + 1
                    curCost[j] = thisCost
    print curCost
    return res

def  Circles( distance,  radius,  cost):
    if not cost or not radius: return []
    tupleData = []
    for i in xrange(len(radius)):
        tupleData.append([i+1, radius[i], cost[i], float('inf'), 0])
    tupleData.sort(key = lambda x: x[1])
    left = 0
    right = len(tupleData) - 1
    while left < len(tupleData):
        while right >= left and tupleData[left][1] + tupleData[right][1] >= distance:
            thisCost = tupleData[left][2] + tupleData[right][2]
            if thisCost < tupleData[left][3]:
                tupleData[left][3] = thisCost
                tupleData[left][4] = tupleData[right][0]
            if thisCost < tupleData[right][3]:
                tupleData[right][3] = thisCost
                tupleData[right][4] = tupleData[left][0]
            right -= 1
        left += 1
        right = len(tupleData) - 1
    res = [0] * len(radius)
    for data in tupleData:
        res[data[0]-1] = data[4]
    return res


distance = 8
radius = [1, 3, 6, 2, 5]
cost = [5, 6, 8, 3, 4]
print Circles(distance, radius, cost)
