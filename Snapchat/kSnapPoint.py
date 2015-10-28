class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def printPoint(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'

class Solution:
    def isSnapPoint(self, point, k):
        x = abs(point.x)
        y = abs(point.y)
        digitSum = 0
        while x > 0:
            digitSum += x % 10
            x /= 10
        while y > 0:
            digitSum += y % 10
            y /= 10
        return digitSum <= k

    def reachablePoints(self, k):
        if k < 0: return set()
        pointSet = set([(0, 0)])
        # if k < 0: return pointSet
        # self.helper(pointSet, k, Point(0,0))
        queue = [Point(0, 0)]
        while queue:
            point = queue.pop(0)

            rightPoint = Point(point.x+1, point.y)
            if (rightPoint.x, rightPoint.y) not in pointSet and self.isSnapPoint(rightPoint, k):
                queue.append(rightPoint)
                pointSet.add((rightPoint.x, rightPoint.y))
            leftPoint = Point(point.x-1, point.y)
            if (leftPoint.x, leftPoint.y) not in pointSet and self.isSnapPoint(leftPoint, k):
                queue.append(leftPoint)
                pointSet.add((leftPoint.x, leftPoint.y))
            upPoint = Point(point.x, point.y+1)
            if (upPoint.x, upPoint.y) not in pointSet and self.isSnapPoint(upPoint, k):
                queue.append(upPoint)
                pointSet.add((upPoint.x, upPoint.y))
            downPoint = Point(point.x, point.y-1)
            if (downPoint.x, downPoint.y) not in pointSet and self.isSnapPoint(downPoint, k):
                queue.append(downPoint)
                pointSet.add((downPoint.x, downPoint.y))
        return pointSet

    # def helper(self, pointSet, k, point):
    #     if not self.isSnapPoint(point, k): return
    #     pointSet.add(point)
    #     rightPoint = Point(point.x+1, point.y)
    #     if rightPoint not in pointSet: self.helper(pointSet, k, rightPoint)
    #     leftPoint = Point(point.x-1, point.y)
    #     if leftPoint not in pointSet: self.helper(pointSet, k, leftPoint)
    #     upPoint = Point(point.x, point.y+1)
    #     if upPoint not in pointSet: self.helper(pointSet, k, upPoint)
    #     downPoint = Point(point.x, point.y-1)
    #     if downPoint not in pointSet: self.helper(pointSet, k, downPoint)

solution = Solution()
point = Point(-101, 12)
print Point(1,1)
print Point(1,1)
points = solution.reachablePoints(3)
for point in points:
    print point
