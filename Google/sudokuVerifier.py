# Enter your code here. Read input from STDIN. Print output to STDOUT

def sudokuVerifier(nums):
    if not nums or len(nums) != 81: return 0
    print 'hehe'

    def isValidRow(matrix):
        for row in matrix:
            if not isValidUnit(row):
                return False
        return True

    def isValidCol(matrix):
        for i in range(len(matrix[0])):
            col = []
            for j in range(len(matrix)):
                col.append(matrix[j][i])
            if not isValidUnit(col):
                return False
        return True

    def isValidBox(matrix):
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                box = []
                for x in range(3):
                    for y in range(3):
                        box.append(matrix[i+x][j+y])
                if not isValidUnit(box):
                    return False
        return True

    def isValidUnit(nums):
        numSet = set()
        for n in nums:
            if n not in numSet:
                numSet.add(n)
            else:
                return False
        return True

    matrix = []
    for i in range(0, 81, 9):
        temp = nums[i:i+9]
        matrix.append(temp)
    print matrix
    if not isValidRow(matrix):
        return 0
    elif not isValidCol(matrix):
        return 0
    elif not isValidBox(matrix):
        return 0
    else:
        return 1

nums = raw_input()
print sudokuVerifier(nums)
