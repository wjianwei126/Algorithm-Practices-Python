class MovingWindow:
    def __init__(self, windowSize, stream):
        self.stream = stream
        self.size = windowSize
        self.index = 0
        self.window = []
        self.sum = 0

    def next(self):
        if self.index == len(self.stream):
            drop = self.window.pop(0)
            self.sum -= drop
        elif len(self.window) < self.size:
            self.window.append(self.stream[self.index])
            self.sum += self.stream[self.index]
            self.index += 1
        else:
            drop = self.window.pop(0)
            self.window.append(self.stream[self.index])
            self.sum = self.sum - drop + self.stream[self.index]
            self.index += 1
        return float(self.sum) / len(self.window)

    def hasNext(self):
        return self.index < len(self.stream) or len(self.window) > 1


windowSize = 3
stream = [1,4,5,3,5,7,8,3,2,1,6,9]
window = MovingWindow(windowSize, stream)
while window.hasNext():
    print window.next()
