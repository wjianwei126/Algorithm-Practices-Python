import heapq
def findFreqGreaterThanK(lists, k):
    if not lists: return []
    res = []
    heap = []
    for i in range(len(lists)):
        if len(lists[i]) == 0:
            continue
        heapq.heappush(heap, (lists[i][0], i))

    while len(heap) >= k:
        curVal = None
        count = 0
        curLen = len(heap)
        for i in range(curLen):
            val, index = heapq.heappop(heap)
            if not curVal:
                curVal = val
            if curVal == val:
                count += 1
                while lists[index] and lists[index][0] == curVal:
                    lists[index].pop(0)
                if lists[index]:
                    heapq.heappush(heap, (lists[index][0], index))
            else:
                heapq.heappush(heap, (lists[index][0], index))
                break
        # print 'end round: ', curVal, heap, count
        if count >= k:
            res.append(curVal)

    return res

lists = [[1,2,3,4,5,6,7,8,9,10], [1], [1,2,4,5,7,8,10], [2,4], [1,3,4,6,7,9,10]]
print findFreqGreaterThanK(lists, 4)
