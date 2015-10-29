class ArrayList:
    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.index = 0

    def add(self, element):
        if len(self.array) + 1 == self.capacity:
            self.capacity = self.capacity + self.capacity / 2
            newArray = [None] * self.capacity
            for i in range(self.index+1):
                newArray[i] = self.array[i]
            self.index += 1
            newArray[self.index] = element
            self.array = newArray
        else:
            self.array[self.index] = element
            self.index += 1

    def get(self, i):
        return self.array[i]

    def remove(self, element):
        i = 0
        while i < len(self.array) and self.array[i] != None and self.array[i] != element:
            i += 1
        while i < len(self.array) - 1:
            self.array[i] = self.array[i+1]
            i += 1
        self.array[i] = None
    
