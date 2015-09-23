# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        intervals.sort(key = lambda x: x.start)
        re = []
        for inter in intervals:
            if re and inter.start <= re[-1].end:
                re[-1].end = max(re[-1].end, inter.end)
            else:
                re.append(inter)
        return re

if __name__ == '__main__':
    solu = Solution()
    intervals = [Interval(1,4), Interval(1,5)]
    res = solu.merge(intervals)
