# http://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=143339&extra=page%3D1%26filter%3Dsortid%26sortid%3D311%26searchoption%5B3046%5D%5Bvalue%5D%3D1%26searchoption%5B3046%5D%5Btype%5D%3Dradio%26sortid%3D311

class Event:
    def __init__(self, start, end, id):
        self.start = start
        self.end = end
        self.id = id

class Solution:
    def conflictEvents(self, events):
        if not events or len(events) == 1: return []
        events.sort(key = lambda x: x.start)

        end = events[0].end
        id = events[0].id
        res = []
        for i in range(1, len(events)):
            if events[i].start >= end:
                end = events[i].end
                id = events[i].id
            else:
                if not res:
                    res.append(id)
                res.append(events[i].id)
                end = max(end, events[i].end)
        return res


solu = Solution()
A = Event(0, 4, 0)
B = Event(7, 8, 1)
C = Event(3, 5, 2)
D = Event(3, 4, 3)
E = Event(8, 10, 4)
events = [A, B, C, D, E]
print solu.conflictEvents(events)
