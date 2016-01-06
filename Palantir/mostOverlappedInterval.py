def mostOverlappedInterval(intervals):
    timePoints = []
    start = intervals[0][0]
    end = intervals[0][1]
    for inter in intervals:
        timePoints.append((inter[0], True))
        timePoints.append((inter[1], False))

    timePoints.sort(key=lambda x: x[0])

    curTime = None
    curOverlapNum = 0
    maxOverlapNum = 0


    for time in timePoints:
        if not curTime:
            curTime = time[0]
            curOverlapNum += 1
        else:
            if time[1]:
                curOverlapNum += 1
                curTime = time[0]
            else:
                if curOverlapNum > maxOverlapNum:
                    maxOverlapNum = curOverlapNum
                    start = curTime
                    end = time[0]
                curOverlapNum -= 1

    return (start, end), maxOverlapNum

intervals = [(1, 7), (2, 8), (0, 3), (6, 10), (5, 7)]
intervals = [(1, 7), (6, 7)]
print mostOverlappedInterval(intervals)
