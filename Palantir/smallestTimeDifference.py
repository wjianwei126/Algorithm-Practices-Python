def getMinDiff(h1, m1, h2, m2):
    if h1 > h2:
        diff1 = h1 * 60 + m1 - h2 * 60 - m2
        diff2 = (h2 + 24) *60 + m2 - h1 * 60 - m1
        return min(diff1, diff2)
    elif h1 < h2:
        return getMinDiff(h2, m2, h1, m1)
    else:
        return abs(m1 - m2)
def getMinTimeDiff(timeList):
    if len(timeList) <= 1: return None

    def mycmp(x, y):
        if x[0] > y[0]:
            return 1
        elif x[0] == y[0]:
            if x[1] > y[1]: return 1
            elif x[1] == y[1]: return 0
            else: return -1
        else:
            return -1

    timeList.sort(cmp=mycmp)

    minDiff = float('inf')
    for i in range(1, len(timeList)):
        minDiff = min(minDiff, getMinDiff(timeList[i][0], timeList[i][1], timeList[i-1][0], timeList[i-1][1]))
    minDiff = min(minDiff, getMinDiff(timeList[0][0], timeList[0][1], timeList[-1][0], timeList[-1][1]))
    return minDiff


print getMinDiff(23, 55, 0, 4)
print getMinDiff(20, 4, 20, 47)
print getMinDiff(5, 55, 10, 4)
timeList = [(23, 55), (0, 4), (20, 4), (20, 47), (5, 55), (10, 4)]
print getMinTimeDiff(timeList)
