import random
class BloomFilter:
    def __init__(self, size, hashCount):
        self.size = size
        self.hashCount = hashCount
        self.bitArray = [0] * self.size

    def add(self, s):
        for seed in range(self.hashCount):
            index = self.hashFunction(s, seed) % self.size
            self.bitArray[index] = 1

    def find(self, s):
        for seed in range(self.hashCount):
            index = self.hashFunction(s, seed) % self.size
            if self.bitArray[index] == 0:
                return False
        return True

    def hashFunction(self, s, seed):
        random.seed(seed)
        return hash(s)^random.getrandbits(32)

bloomfilter = BloomFilter(20000, 2)
bloomfilter.add('snap')
bloomfilter.add('chat')
bloomfilter.add('hello')
bloomfilter.add('world')
print bloomfilter.find('snap')
print bloomfilter.find('world')
print bloomfilter.find('python')
