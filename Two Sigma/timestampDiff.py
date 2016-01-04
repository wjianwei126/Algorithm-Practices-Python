from threading import Thread
import threading

class Stream:
    def __init__(self, nums):
        self.nums = nums
        self.index = 0

    def getNext(self):
        if self.index < len(self.nums):
            self.index += 1
            return self.nums[self.index-1]
        else:
            raise

res = []
q1 = []
q2 = []
threadLock = threading.Lock()

def calculatePairs(q1, q2, value):
    q1.append(value)
    # print q1, q2
    while q2 and value - q2[0] >= 1:
        q2.pop(0)
    for num in q2:
        if abs(num - value) < 1:
            res.append((value, num))

s1 = Stream([0.2, 1.4, 3.0])
s2 = Stream([2.0, 2.1, 4.5])
def Q1Thead(s):
    while True:
        try:
            value = s.getNext()
            threadLock.acquire()
            calculatePairs(q1, q2, value)
            threadLock.release()
        except:
            break

def Q2Thead(s):
    while True:
        try:
            value = s.getNext()
            threadLock.acquire()
            calculatePairs(q2, q1, value)
            threadLock.release()
        except:
            break

try:
    new_thread1=Thread(target = Q1Thead, args = (s1,))
    new_thread1.setDaemon(True)
    new_thread1.start()
    new_thread2=Thread(target = Q2Thead, args = (s2,))
    new_thread2.setDaemon(True)
    new_thread2.start()
except:
   print "Error: unable to start thread"

print res
