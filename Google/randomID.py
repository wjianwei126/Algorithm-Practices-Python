import random
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class MyRandom:
    def __init__(self, ids, probabilities):
        # O(n) time O(n) Space
        self.totalIDs = len(ids)
        self.idMap = {}
        self.dic = {}
        prob = 0
        for i in range(self.totalIDs):
            self.idMap[i] = ids[i]
            self.dic[i] = Interval(prob, prob+probabilities[i])
            prob += probabilities[i]

    def genRandom(self):
        # time O(logn)
        randomNum = random.random()
        print randomNum
        left = 0
        right = self.totalIDs - 1
        while left <= right:
            mid = left + (right - left) / 2
            interval = self.dic[mid]
            if randomNum >= interval.start and randomNum < interval.end:
                return self.idMap[mid]
            elif randomNum < interval.start:
                right = mid - 1
            else:
                left = mid + 1

ids = ['A', 'B', 'C']
probabilities = [0.2, 0.3, 0.5]
myRandom = MyRandom(ids, probabilities)
dic = {'A':0, 'B':0, 'C':0}
for i in range(100000):
    key = myRandom.genRandom()
    dic[key] += 1

print dic
