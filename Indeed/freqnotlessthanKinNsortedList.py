import heapq
class Stream:
    def __init__(self, inputList):
        self.list = inputList
        self.index = 0

    def hasNext(self):
        return self.index < len(self.list)

    def next(self):
        if not self.hasNext():
            raise IndexError('No more value!')
        self.index += 1
        return self.list[self.index-1]

def findFreqGreaterThanK(streams, k):
    if not streams: return []
    res = []
    heap = []
    for i in range(len(streams)):
        if not streams[i].hasNext():
            continue
        heapq.heappush(heap, (streams[i].next(), i))

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
                if streams[index].hasNext():
                    nextValue = streams[index].next()
                    while streams[index].hasNext() and nextValue == curVal:
                        nextValue = streams[index].next()
                    if nextValue != curVal:
                        heapq.heappush(heap, (nextValue, index))
            else:
                heapq.heappush(heap, (val, index))
                break

        if count >= k:
            res.append(curVal)

    return res

s1 = Stream([1,2,3,4,5,6,7,8,9,10])
s2 = Stream([1])
s3 = Stream([1,2,4,5,7,8,10])
s4 = Stream([2,4])
s5 = Stream([1,3,4,6,7,9,10])
print findFreqGreaterThanK([s1,s2,s3,s4,s5], 4)
