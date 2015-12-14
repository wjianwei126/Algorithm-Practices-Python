class ListIterator:
    def __init__(self, inputList):
        if not inputList or len(inputList) == 0:
            self.temp = None
            return
        self.inputList = inputList
        self.index = 0
        self.subIterator = None
        while self.index < len(inputList):
            if isinstance(inputList[self.index], list):
                self.subIterator = ListIterator(inputList[self.index])
                if self.subIterator.hasNext():
                    self.temp = self.subIterator.next()
                    self.index += 1
                    return
                else:
                    self.subIterator = None
                    self.index += 1
            else:
                self.temp = inputList[self.index]
                self.index += 1
                return
        self.temp = None

    def hasNext(self):
        if not self.temp:
            return False
        else:
            return True

    def next(self):
        returnValue = self.temp
        find = False

        if self.subIterator and self.subIterator.hasNext():
            self.temp = self.subIterator.next()
            find = True
        else:
            self.subIterator = None
            while self.index < len(self.inputList):
                if isinstance(self.inputList[self.index], list):
                    self.subIterator = ListIterator(inputList[self.index])
                    if self.subIterator.hasNext():
                        self.temp = self.subIterator.next()
                        self.index += 1
                        find = True
                        break
                    else:
                        self.subIterator = None
                        self.index += 1
                else:
                    self.temp = self.inputList[self.index]
                    self.index += 1
                    find = True
                    break
        if not find:
            self.temp = None
        return returnValue

inputList = [1, 2, [3, 4, 5]]
inputList = [[1], 2, [[3,4], 5], [[[]]], [[[6]]], 7, 8, []]
inputList = [[[]], 1]
iterator = ListIterator(inputList)
while iterator.hasNext():
    print iterator.next()
