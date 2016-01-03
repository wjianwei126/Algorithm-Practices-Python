class RandomIterator:
    def __init__(self):
        self.index = 0
        self.list = [1,6,5,10,-3,6,12,15]
        self.list = []

    def hasNext(self):
        return self.index < len(self.list)

    def next(self):
        self.index += 1
        return self.list[self.index-1]

    def remove(self):
        pass

class ModFiveIterator:
    def __init__(self):
        self.temp = None
        self.randomIterator = RandomIterator()

    def next(self):
        if not self.hasNext():
            raise IndexError('End of Iterator!')
        return self.temp

    def hasNext(self):
        if self.randomIterator.hasNext():
            self.temp = self.randomIterator.next()
            while self.temp % 5 != 0 and self.randomIterator.hasNext():
                self.temp = self.randomIterator.next()
            if self.temp % 5 != 0:
                return False
            return True
        else:
            return False

myIterator = ModFiveIterator()
print myIterator.next()
print myIterator.next()
print myIterator.next()
print myIterator.next()
print myIterator.next()
