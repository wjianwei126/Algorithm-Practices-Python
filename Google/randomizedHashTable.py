import random
class RandomizeHashTable:
    def __init__(self):
        self.keyDic = {}  # key: value
        self.indexDic = {} # key: index
        self.keyList = [] # key

    def put(self, key, value):
        if key in self.keyDic:
            self.keyDic[key] = value
        else:
            self.keyDic[key] = value
            self.indexDic[key] = len(self.keyList)
            self.keyList.append(key)

    def get(self, key):
        if key not in self.keyDic:
            raise ValueError('Key not in the table')
        else:
            return self.keyDic[key]

    def delete(self, key):
        if key not in self.keyDic:
            raise ValueError('Key not in the table')
        else:
            del self.keyDic[key]
            delIndex = self.indexDic[key]   # indexDic is only used here
            self.indexDic[self.keyList[-1]] = delIndex
            del self.indexDic[key]
            self.keyList[delIndex], self.keyList[-1] = self.keyList[-1], self.keyList[delIndex]
            self.keyList.pop()

    def getRandom(self):
        rand = random.randint(0, len(self.keyList)-1)
        return self.keyDic[self.keyList[rand]]
