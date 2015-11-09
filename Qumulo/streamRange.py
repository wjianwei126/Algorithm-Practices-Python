class Stream:
    def __init__(self):
        self.parents = {}

    def find(self, x):
        return self.parents[x]

    def union(self, x, y):
        parent = self.parents[x]
        if parent == self.parents[y]:
            return False
        for i in self.parents.keys():
            if self.parents[i] == parent:
                self.parents[i] = self.parents[y]

    def addNum(self, num):
        # O(n)
        if num in self.parents:
            return
        self.parents[num] = num
        if num + 1 in self.parents:
            self.union(num+1, num)
        if num - 1 in self.parents:
            self.union(num-1, num)

    def getRange(self):
        # O(n)
        ranges = {}
        for num in self.parents:
            if self.parents[num] not in ranges:
                ranges[self.parents[num]] = [num, num]
            else:
                curMin, curMax = ranges[self.parents[num]]
                ranges[self.parents[num]] = [min(curMin, num), max(curMax, num)]
        res = []
        for rangeSet in ranges:
            rangeMin, rangeMax = ranges[rangeSet]
            if rangeMin == rangeMax:
                res.append(str(rangeMin))
            else:
                res.append(str(rangeMin) + '-' + str(rangeMax))
        return res

stream = Stream()
stream.addNum(8)
print stream.getRange()
stream.addNum(6)
print stream.getRange()
stream.addNum(4)
print stream.getRange()
stream.addNum(7)
print stream.getRange()
