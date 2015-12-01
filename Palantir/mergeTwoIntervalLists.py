class Solution:
    def unionTwoLists(self, l1, l2):
        if not l1: return l2
        if not l2: return l1
        res = []
        p1 = p2 = 0
        while p1 < len(l1) or p2 < len(l2):
            if p1 == len(l1) or p2 < len(l2) and l2[p2][0] < l1[p1][0]:
                (start, stop) = l2[p2]
                p2 += 1
            else:
                (start, stop) = l1[p1]
                p1 += 1

            if not res or res[-1][1] < start:
                res.append([start, stop])
            else:
                res[-1][1] = max(res[-1][1], stop)

        return res

    def interTwoLists(self, l1, l2):
        if not l1: return l2
        if not l2: return l1
        res = []
        p1 = p2 = 0
        startF1 = startF2 = 0
        count = 0
        while p1 < len(l1) or p2 < len(l2):
            if p1 == len(l1) or p2 < len(l2) and l2[p2][startF2] < l1[p1][startF1]:
                cur = l2[p2][startF2]
                if startF2 == 0:
                    startPoint = True
                    startF2 = 1
                else:
                    startPoint = False
                    startF2 = 0
                    p2 += 1
            else:
                cur = l1[p1][startF1]
                if startF1 == 0:
                    startPoint = True
                    startF1 = 1
                else:
                    startPoint = False
                    startF1 = 0
                    p1 += 1

            if startPoint:
                count += 1
                if count == 2:
                    start = cur
            else:
                count -= 1
                if count == 1:
                    if cur == start:
                        res.append((cur))
                    else:
                        res.append([start, cur])

        return res

l1 = [(1, 3), (6, 7), (10, 15)]
l2 = [(2, 3), (4, 6), (9, 11), (12, 17)]
solution = Solution()
print solution.unionTwoLists(l1, l2)
print solution.interTwoLists(l1, l2)
