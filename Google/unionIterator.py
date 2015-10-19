class Iterator:
    def __init__(self, nums):
        self.nums = nums
        self.index = 0
    def hasNext(self):
        if self.index >= len(self.nums):
            return False
        else:
            return True
    def next(self):
        self.index += 1
        return self.nums[self.index-1]

class UnionIterator:
    def __init__(self, iterator1, iterator2):
        self.iterator1 = iterator1
        self.iterator2 = iterator2
        self.outputSet = set()
        if self.iterator1.hasNext():
            self.temp = iterator1.next()
        elif self.iterator2.hasNext():
            self.temp = iterator2.next()
        else:
            self.temp = None

    def hasNext(self):
        return self.temp != None

    def next(self):
        current = self.temp
        self.outputSet.add(current)

        while self.iterator1.hasNext() or self.iterator2.hasNext():
            if self.iterator1.hasNext():
                self.temp = self.iterator1.next()
            elif self.iterator2.hasNext():
                self.temp = self.iterator2.next()
            else:
                self.temp = None
                break

            if self.temp not in self.outputSet:
                break

        if not self.iterator1.hasNext() and not self.iterator2.hasNext() and self.temp in self.outputSet:
            self.temp = None
        return current

it1 = Iterator([3,4,5])
it2 = Iterator([1,5])
union = UnionIterator(it1, it2)
while union.hasNext():
    print union.next()
