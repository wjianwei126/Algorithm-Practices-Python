class FileReader(object):
    def __init__(self):
        self.cache = []

    def read4(self, buff):
        # Provided API
        pass

    def readN(self, buff, n):
        # call once
        idx = 0
        while True:
            buff4 = [''] * 4
            readLen = min(self.read4(buff4), n - idx)
            for i in range(readLen):
                buff[idx] = buff4[i]
                idx += 1
            if readLen < 4:
                return idx

    def readNMultiCall(self, buff, n):
        # call multiple times
        idx = 0
        while True:
            buff4 = [''] * 4
            readLen = self.read4(buff4)
            for i in range(readLen):
                self.cache.append(buff4[i])
            while idx < n and self.cache:
                buff[idx] = self.cache.pop(0)
                idx += 1
            if readLen < 4 or idx == n:
                return idx

    def seek(self, buff, k, n):
        # read n characters from position k
        buffK = [''] * k
        tmp = self.readNMultiCall(buffK, k)
        if tmp < k:
            return 0
        return self.readNMultiCall(buff, n)
