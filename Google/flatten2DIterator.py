# Implement an iterator to flatten a 2d vector.
#
# For example,
# Given 2d vector =
#
# [
#   [1,2],
#   [3],
#   [4,5,6]
# ]
# By calling next repeatedly until hasNext returns false,
# the order of elements returned by next should be: [1, 2, 3, 4, 5, 6].
class ArraysIterator:
    def __init__(self, lists):
        if not lists:
            raise ValueError('Invalid input')
        self.row = len(lists)
        self.lists = lists
        self.curRow = 0

        # while self.curRow < self.row and len(self.lists[self.curRow]) == 0:
        #     self.curRow += 1
        # if self.curRow == self.row:
        #     raise ValueError('Invalid input')

        self.curCol = 0


    def hasNext(self):
        return self.curRow != self.row

    def next(self):
        curValue = self.lists[self.curRow][self.curCol]
        self.curCol += 1
        if self.curCol == len(self.lists[self.curRow]):
            self.curCol = 0
            self.curRow += 1

        # while self.curRow < self.row and len(self.lists[self.curRow]) == 0:
        #     self.curRow += 1

        return curValue

nums = [[1, 2], [3], [4, 5, 6]]
# nums = [[], [], [3, 4, 5]]
iterator = ArraysIterator(nums)
while iterator.hasNext():
    print iterator.next()
