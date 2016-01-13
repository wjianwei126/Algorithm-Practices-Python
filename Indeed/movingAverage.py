class AverageQueue:
    QUEUE_INTERVAL = 5 * 60
    def __init__(self):
        self.sum = 0
        self.queue = []

    def getNow(self):
        return time.time()

    def record(self, value):
        now = self.getNow()
        self.popQueue(now)
        self.queue.append((now, value))
        self.sum += value

    def getAvg(self):
        now = self.getNow()
        self.popQueue(now)
        return self.sum * 1.0 / len(self.queue)

    def popQueue(self, now):
        while self.queue and now - self.queue[0][0] > QUEUE_INTERVAL:
            deleted = self.queue.pop(0)
            self.sum -= deleted[1]
            
