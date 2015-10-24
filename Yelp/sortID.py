import heapq
def sortIDs():
    heap = []
    pair = raw_input()
    while pair:
        value, id = pair.split()
        heapq.heappush(heap, (-int(id), value))
        pair = raw_input()

    while heap:
        pair = heapq.heappop(heap)
        id = -pair[0]
        value = pair[1]
        print value + ' ' + str(id)

sortIDs()
