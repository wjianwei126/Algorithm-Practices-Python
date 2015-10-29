# 先是建一个event, 里面有start time和end time, 然后check这两个event有没有conflict,
# 各种if else, 然后升级, 给一个list of events, 直接sort他们。再升级, 建一个schedule,
# 给几个office, 问怎么样的solution才是optimal的
import heapq
class Event:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Schedule:
    def __init__(self):
        self.eventList = []

    def addEvent(self, event):
        self.eventList.append(event)

    def hasConflict(self, event1, event2):
        if event1.start > event2.end or event1.end < event2.start:
            return False
        else:
            return True

    def sortEvents(self):
        self.eventList.sort(key=lambda x: x.end)

    def schedule(self):
        self.sortEvents()
        heap = []
        heapq.heappush(heap, (self.eventList[0].end, [self.eventList[0]]))
        for i in range(1, len(self.eventList)):
            earliest = heap[0][0]
            if self.eventList[i].start < earliest:
                heapq.heappush(heap, (self.eventList[i].end, [self.eventList[i]]))
            else:
                endTime, office = heapq.heappop(heap)
                office.append(self.eventList[i])
                heapq.heappush(heap, (self.eventList[i].end, office))
        res = []
        while heap:
            res.append(heapq.heappop(heap)[1])
        return res

schedule = Schedule()
E1 = Event(1, 5)
E2 = Event(3, 4)
E3 = Event(6, 7)
E4 = Event(3, 9)
E5 = Event(6.5, 10)
schedule.addEvent(E1)
schedule.addEvent(E2)
schedule.addEvent(E3)
schedule.addEvent(E4)
schedule.addEvent(E5)
res = schedule.schedule()
for office in res:
    print '-'
    for event in office:
        print str(event.start) + '-' + str(event.end)
