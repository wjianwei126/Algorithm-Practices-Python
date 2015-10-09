class TimeTravelingHashTable:
    def __init__(self):
        self.dic = {}

    def insert(self, key, value, timestamp):
        if key not in self.dic:
            self.dic[key] = [(timestamp, value)]
        else:
            self.dic[key].insert(0, (timestamp, value))

    def get(self, key, timestamp = None):
        if key not in self.dic:
            return -1
        if not timestamp:
            return self.dic[key][0][1]

        values = self.dic[key]
        left = 0
        right = len(values) - 1
        while left <= right:
            mid = left + (right - left) / 2
            if values[mid][0] == timestamp:
                return values[mid][1]
            elif values[mid][0] > timestamp:
                left = mid + 1
            else:
                right = mid - 1
        return values[left][1]

table = TimeTravelingHashTable()
table.insert('k1', 'v1', 10)
print table.get("k1")
print table.get("k1", 11)
table.insert("k1", "v2", 20)
print table.get("k1", 15)
print table.get("k1", 11)
print table.get("k1", 24)
table.insert('k1', 'v3', 30)
print table.get('k1', 24)
print table.get('k1')
