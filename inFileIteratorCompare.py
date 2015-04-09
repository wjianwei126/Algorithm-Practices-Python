# compare two file iterator, determine if the distance between them is at most 1
# Distance: minimum number of modifications to make a=b
# Modification:
#   1. change an int in a
#   2. insert an int to a
#   3. remove an int from a

class IntFileIterator:
	def __init__(self, array):
		self.array = array
		self.count = -1
	def hasNext(self):
		return self.count < len(self.array) - 1
	def next(self):
		self.count += 1
		return self.array[self.count]


class FileCompare:
	'''
	def isDistanceZeroOrOne(self, fileIterator1, fileIterator2):
		if not fileIterator1 and fileIterator2: return False
		if not fileIterator2 and fileIterator1: return False
		if not fileIterator1 and not fileIterator2: return True
		return self.distanceHelper(fileIterator1, fileIterator2, 0)

	def distanceHelper(self, iterator1, iterator2, count):
		if count > 1: 
			return False
		if (not iterator1.hasNext() and not iterator2.hasNext()):
			return True

		if iterator1.hasNext() and not iterator2.hasNext():
			iterator1.next()
			return self.distanceHelper(iterator1, iterator2, count+1)
		elif not iterator1.hasNext() and iterator2.hasNext():
			iterator2.next()
			return self.distanceHelper(iterator1, iterator2, count+1)
		else:
			if iterator1.next() == iterator2.next():
				return self.distanceHelper(iterator1, iterator2, count)
			else:
				return self.distanceHelper(iterator1, iterator2, count+1)

	def nonrecursive(self, fileIterator1, fileIterator2):
		if not fileIterator1 and fileIterator2: return False
		if not fileIterator2 and fileIterator1: return False
		if not fileIterator1 and not fileIterator2: return True
		totalModi = 0
		while fileIterator1.hasNext() or fileIterator2.hasNext():

			if fileIterator1.hasNext() and  not fileIterator2.hasNext():
				iterator1.next()
				totalModi += 1

			elif not fileIterator1.hasNext() and fileIterator2.hasNext():
				iterator2.next()
				totalModi += 1

			else:
				if fileIterator1.next() != fileIterator2.next():
					totalModi += 1

			if totalModi > 1:
				return False
		return True
	'''
	def rightmethod(self, fileIterator1, fileIterator2):
		if not fileIterator1 and fileIterator2: return False
		if not fileIterator2 and fileIterator1: return False
		if not fileIterator1 and not fileIterator2: return True
		isSame = True            # always the same so far
		isChanged = False        # if only one change made can make two iterator the same
		isAdd = False            # if iterator2 add one item can be the same as iterator1
		isRemove = False         # if iterator2 remove one item can be the same as iterator2

		addRemoveFlag = False
		changeFlag = False       # to mark whether we have made changes

		cur1 = cur2 = 0

		while fileIterator1.hasNext() and fileIterator2.hasNext():
			prev1 = cur1
			prev2 = cur2
			cur1 = fileIterator1.next()
			cur2 = fileIterator2.next()
			if cur1 != cur2:

				if isSame:
					isSame = False

				if not changeFlag:
					changeFlag = True
					isChanged = True
				else:					# this means we need more than 1 change
					isChanged = False


				if not addRemoveFlag:
					addRemoveFlag = True
					isAdd = True
					isRemove = True
					continue

			# here means there is at least one difference may need to be considered add or remove
			if addRemoveFlag:
				isAdd = isAdd and (cur1 == prev2)
				isRemove = isRemove and (cur2 == prev1)

			if not (isSame or isAdd or isRemove or isChanged):
				return False

		if fileIterator1.hasNext():
			tail1 = fileIterator1.next()
			return (isSame or (isAdd and tail1 == cur2)) and not fileIterator1.hasNext()

		if fileIterator2.hasNext():
			tail2 = fileIterator2.next()
			return (isSame or (isRemove and tail2 == cur1)) and not fileIterator2.hasNext()

		return isSame or isChanged




if __name__ == "__main__":
	fileIter1 = IntFileIterator([1,2,3,4])
	fileIter2 = IntFileIterator([1,2,3,4,5])
	'''
	test cases:

	s1=[1 2 1] ,s2=2 1 2 :false
	s1=1 2 1 ,s2=2 1 2 1 :true
	s1=1 2 1 2 ,s2=2 1 2 1 3 :false
	s1=1 2 1 2 ,s2=2 1 2 :true
	s1=1 2 1 3 ,s2=2 1 2 :false
	s1=[] ,s2= :true
	s1=[] ,s2=1 :true
	s1= ,s2=1 1 :false

	'''
	comparator = FileCompare()
	print comparator.rightmethod(fileIter1, fileIter2)

