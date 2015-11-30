class FixedLenQueue:
    def __init__(self, length):
        self.length = length
        self.head = -1
        self.tail = -1
        self.full = False
        self.queue = [None] * self.length

    def push(self, element):
        if self.full:
            raise MemoryError('The queue is full')

        self.tail = (self.tail + 1) % self.length
        if self.tail == self.head:
            self.full = True
        self.queue[self.tail] = element

    def pop(self):
        if self.tail == self.head and not self.full:
            raise MemoryError('The queue is empty')

        self.head = (self.head + 1) % self.length
        self.full = False
        return self.queue[self.head]

fq = FixedLenQueue(3)
# print fq.pop()
fq.push(1)
fq.push(2)
print fq.pop()
fq.push(3)
fq.push(4)
print fq.queue
print fq.pop()
fq.push(6)
