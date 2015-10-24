import math
class Solution:
    def pointEdgeParts(self, point, edge, relations):
        if not relations: return 0

        points = set(range(1, point+1))

        edgeDic = {i: set() for i in range(1, point+1)}
        for i in xrange(edge):
            thisEdge = relations[i]
            edgeDic[thisEdge[0]].add(thisEdge[1])
            edgeDic[thisEdge[1]].add(thisEdge[0])
        print edgeDic

        parts = []
        for i in xrange(1, point+1):
            if i in points:
                points.remove(i)
                part = [i]
                connect = edgeDic[i]
                while connect:
                    neighbor = connect.pop()
                    if neighbor in points:
                        points.remove(neighbor)
                        connect = connect.union(edgeDic[neighbor])
                        part.append(neighbor)
                parts.append(part)

        print parts
        res = 0
        for part in parts:
            res += int(math.ceil(math.sqrt(len(part))))
        return res

solution = Solution()
print solution.pointEdgeParts(4, 3, [(1,2), (1,4), (2,3)])
