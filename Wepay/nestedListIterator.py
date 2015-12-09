class DataNode:
    def __init__(self, isList, data):
        self.isList = isList
        self.data = data

class NestedListIterator:
    def __init__(self, node):
        self.node = node
        self.nums = []
        # self.flatten(node)
        self.temp = self.flatten(node)

    def flatten(self, node):
        if node.isList:
            for item in node.data:
                if not item.isList:
                    # self.nums.append(item.data)
                    yield item.data
                else:
                    self.flatten(item)
        else:
            # self.nums.append(item.data)
            yield item.data

    def hasNext(self):
        return self.temp != None

    def next(self):
        temp = self.temp
        self.temp = self.flatten(self.node)
        return temp


N1 = DataNode(False, 1)
N2 = DataNode(False, 2)
N3 = DataNode(False, 3)
N4 = DataNode(False, 4)
N5 = DataNode(False, 5)
N6 = DataNode(False, 6)

N7 = DataNode(True, [N4])
N8 = DataNode(True, [N3, N7, N5])
N9 = DataNode(True, [N1, N2, N8, N6])

nestedList = NestedListIterator(N9)

while nestedList.hasNext():
    print nestedList.next()
