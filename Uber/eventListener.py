class Event(object):
    def __init__ (self, data):
        self.data = data

class EventListener(object):
    def __init__(self):
        self.map = {}

    def registerEvent(self, eventName, event):
        if eventName not in self.map:
            self.map[eventName] = set([event])
        else:
            self.map[eventName].add(event)

    def unregisterEvent(self, eventName, event):
        if eventName in self.map:
            if event in self.map[eventName]:
                self.map[eventName].remove(event)
                if len(self.map[eventName]) == 0:
                    del self.map[eventName]

    def postEvent(self, eventName, data):
        if eventName in self.map:
            for listener in self.map[eventName]:
                event = Event(data)
                self.registerEvent(eventName, event)
