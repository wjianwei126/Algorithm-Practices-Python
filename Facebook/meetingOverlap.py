# Given a array of pairs where each pair contains the start and end time of a meeting (as in int),
# Determine if a single person can attend all the meetings
# Input array(pair(1,4), pair(4, 5), pair(3,4), pair(2,3))
# Output: False
# follow up:
# determine the minimum number of meeting rooms needed to hold all the meetings.
# Input array(pair(1, 4), pair(2,3), pair(3,4), pair(4,5))
# Output: 2
class interval:
    def __init__(self, s, e):
        self.start = s
        self.end = e

class Solution:
    def meetingOverlap(self, intervals):
        if not intervals or len(intervals) == 0: return True
        intervals.sort(cmp = lambda x,y: cmp(x.start, y.start))
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i-1].end:
                return False
        return True

    def maxMeetingRoom(self, intervals):
        if not intervals or len(intervals) == 0: return 0
        start_dict = {}
        end_dict = {}
        allTimes = []
        for i in range(len(intervals)):

            if intervals[i].start not in start_dict:
                start_dict[intervals[i].start] = 1
            else:
                start_dict[intervals[i].start] += 1
            if intervals[i].end not in end_dict:
                end_dict[intervals[i].end] = 1
            else:
                end_dict[intervals[i].end] += 1

            allTimes.append(intervals[i].start)
            allTimes.append(intervals[i].end)
        allTimes.sort()
        count = 0
        maxcount = 0
        for point in allTimes:
            if point in end_dict and end_dict[point] > 0:
                count -= 1
                end_dict[point] -= 1
            if point in start_dict and start_dict[point] > 0:
                count += 1
                maxcount = max(maxcount, count)
                start_dict[point] -= 1
                continue
            

        return maxcount

	
if __name__ == "__main__":
    inter = [interval(1,4), interval(4,5), interval(3,4), interval(2,3)]
    
    solu = Solution()
    print solu.meetingOverlap(inter)
    print solu.maxMeetingRoom(inter)