import time
import datetime

class GoogleMapsClient(object):
    """3rd party maps client; we CANT EDIT THIS."""

    def __init__(self):
        self.requests_made = 0

    def make_request(self):
        self.requests_made += 1
        now = datetime.datetime.now().time()
        return "%d - %s - San Francisco" % (self.requests_made, now)

class MyRequest(object):
    def __init__(self, capacity):
        self.client = GoogleMapsClient()
        self.capacity = capacity
        self.queue = []

    def makeRequest(self):
        now = time.time()
        if len(self.queue) < self.capacity:
            self.queue.append(now)
            print self.client.make_request()
        elif now - self.queue[0] > 1:
            self.queue.pop(0)
            self.queue.append(now)
            print self.client.make_request()
        else:
            return

user = MyRequest(10)
for i in range(40):
    time.sleep(0.05)
    user.makeRequest()
