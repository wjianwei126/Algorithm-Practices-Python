# implement a queue using two stacks

class Solution:
    def __init__(self):
        self.inbox = []
        self.outbox = []
    def enqueue(self, x):
        self.inbox.append(x)
    def dequeue(self):
        if not self.outbox:
            while self.inbox:
                self.outbox.append(self.inbox.pop())
        return self.outbox.pop()

if __name__ == "__main__":
    solu = Solution()
    print solu.enqueue("a")
    print solu.enqueue("b")
    print solu.enqueue("c")
    print solu.dequeue()
    print solu.enqueue("d")
    print solu.dequeue()
    print solu.dequeue()
    print solu.dequeue()