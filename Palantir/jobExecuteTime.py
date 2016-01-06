class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Job:
    def __init__(self, label):
        self.label = label
        self.intervals = []

class timeNode:
    def __init__(self, label, start):
        self.label = label
        self.start = start

def getJobList(jobs):
    if not jobs: return
    timeNodeDic = {}
    for job in jobs:
        for interval in job.intervals:
            if interval.start in timeNodeDic:
                timeNodeDic[interval.start].append(timeNode(job.label, True))
            else:
                timeNodeDic[interval.start] = [timeNode(job.label, True)]
            if interval.end in timeNodeDic:
                timeNodeDic[interval.end].append(timeNode(job.label, False))
            else:
                timeNodeDic[interval.end] = [timeNode(job.label, False)]

    timeNodeList = timeNodeDic.keys()
    timeNodeList.sort()

    curExecuteSet = set()
    curTime = None
    for timePoint in timeNodeList:
            if curTime == None:
                curTime = timePoint
                for node in timeNodeDic[timePoint]:
                    curExecuteSet.add(node.label)
            else:
                curJobs = list(curExecuteSet)
                jobText = curJobs[0] if len(curJobs) == 1 else ' and '.join(curJobs)
                if len(curJobs) > 0:
                    print '[' + str(curTime) + ', ' + str(timePoint) + '] is executing ' + jobText
                curTime = timePoint
                for node in timeNodeDic[timePoint]:
                    if node.start:
                        curExecuteSet.add(node.label)
                    else:
                        curExecuteSet.remove(node.label)

jobA = Job('A')
jobB = Job('B')
jobC = Job('C')
jobA.intervals = [Interval(0, 10), Interval(15, 20)]
jobB.intervals = [Interval(5, 10), Interval(11, 12)]
jobC.intervals = [Interval(15, 25)]
jobs = [jobA, jobB, jobC]
getJobList(jobs)
