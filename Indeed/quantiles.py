import time
# def findQuantiles():
#     Q = int(raw_input())
#     M = int(raw_input())
#     inputList = []
#     for i in range(M):
#         value, count = map(int, raw_input().split(' '))
#         inputList += [value] * count
#
#     start = time.time()
#
#     inputList.sort()
#
#     N = len(inputList)
#     for k in range(1, Q):
#         if N * k % Q == 0:
#             index = N * k / Q - 1
#         else:
#             index = int(N * k / Q)
#         print inputList[index]
#
#     print time.time() - start
#
# findQuantiles()

import collections
def findQuantiles2():
    Q = int(raw_input())
    M = int(raw_input())
    inputDict = {}
    N = 0
    for i in range(M):
        value, count = map(int, raw_input().split(' '))
        inputDict[value] = count
        N += count

    start = time.time()
    sortedDict = collections.OrderedDict(sorted(inputDict.items()))
    print sortedDict

    for k in range(1, Q):
        if N * k % Q == 0:
            index = N * k / Q
        else:
            index = int(N * k / Q) + 1
        accumulatedCount = 0
        for key in sortedDict.keys():
            if accumulatedCount + sortedDict[key] < index:
                accumulatedCount += sortedDict[key]
            else:
                print key
                break

    print time.time() - start

findQuantiles2()
