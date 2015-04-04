# given two arrays, the first one is the actual array while the second one is the corresponding positon
# sort the first array by using the second one
# e.g. array1 : [5 0 3 2 8] array2 : [3 0 2 1 4]
# output: [0 2 3 5 8]

class Solution:
    def positionSort(self, l1, l2):
        if not l1 or not l2 or len(l1) == 0 or len(l2) == 0: return []
        if len(l1) != len(l2): return None
        i = 0
        while i < len(l1):
            if l2[i] != i:
                tmp = l2[i]
                tmp2 = l1[i]
                l2[i] = l2[tmp]
                l1[i] = l1[tmp]
                l2[tmp] = tmp
                l1[tmp] = tmp2

                continue
            else:
                i += 1
        return l1

      

if __name__ == "__main__":
    l1 = [5,0,3,2,8]
    l2 = [3,0,2,1,4]
    solu = Solution()
    print solu.positionSort(l1, l2)