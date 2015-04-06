# sort suffix array in lexical order

class Solution:
    def sortSuffix(self, A):
        def comperator(x, y):
            i = 0
            while i < len(x[0]) and i < len(y[0]):
                if x[0][i] == y[0][i]:
                    i += 1
                    continue
                elif x[0][i] > y[0][i]:
                    return 1
                else:
                    return -1
            if i == len(x[0]):
                return -1
            if i == len(y[0]):
                return 1

        suffix = []
        for i in range(len(A)):
            suffix.append((A[i:], i))
        #print suffix
        suffix.sort(comperator)
        re = []
        for i in range(len(suffix)):
            re.append(suffix[i][1])
        return re

    def findSubtext(self, text, subtext):
        def comperator(x, y):
            i = 0
            while i < len(x[0]) and i < len(y[0]):
                if x[0][i] == y[0][i]:
                    i += 1
                    continue
                elif x[0][i] > y[0][i]:
                    return 1
                else:
                    return -1
            if i == len(x[0]):
                return -1
            if i == len(y[0]):
                return 1

        suffix = []
        for i in range(len(text)):
            suffix.append((text[i:], i))
        #print suffix
        suffix.sort(comperator)
        #print suffix
        left = 0
        right = len(suffix) - 1
        while left <= right:
            mid = left + (right - left) / 2
            if suffix[mid][0][0] == subtext[0]:

                i = 0
                flag = True
                while i < len(suffix[mid][0]) and i < len(subtext):
                    if suffix[mid][0][i] != subtext[i]:
                        flag = False
                        break
                    i += 1
                if i == len(suffix[mid][0]) and i < len(subtext):
                    return False
                if flag:
                    return True
                else:
                    return False
            elif suffix[mid][0][0] < subtext[0]:
                right = mid - 1
            else:
                left = mid + 1
        return False
            
        

if __name__ == "__main__":
    solu = Solution()
    A = [10, 20, 30, 25]
    #print solu.sortSuffix(A)
    print solu.findSubtext(A, [20, 30])