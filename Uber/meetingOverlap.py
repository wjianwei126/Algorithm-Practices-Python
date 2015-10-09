class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def meetingOverlap(self, meetings):
        if not meetings: return True
        slots = [False] * 1440
        for meeting in meetings:
            for i in range(meeting.start, meeting.end):
                if slots[i]:
                    return False
                slots[i] = True
        return True

solution = Solution()
A = Interval(1, 40)
B = Interval(40, 50)
print solution.meetingOverlap([A, B])
