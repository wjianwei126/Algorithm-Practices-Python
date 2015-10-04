# http://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=143304&extra=page%3D1%26filter%3Dsortid%26sortid%3D311%26searchoption%5B3046%5D%5Bvalue%5D%3D1%26searchoption%5B3046%5D%5Btype%5D%3Dradio%26sortid%3D311
class BIT:
    def __init__(self, n):
        sz = 1
        while n >= sz:
            sz *= 2
        self.size = sz
        self.sumList = [0]*sz

    def sum(self, i):
        assert i > 0
        s = 0
        while i > 0:
            s += self.sumList[i]
            i -= i & -i
        return s

    def add(self, i, x):
        assert i > 0
        while i < self.size:
            self.sumList[i] += x
            i += i & -i
