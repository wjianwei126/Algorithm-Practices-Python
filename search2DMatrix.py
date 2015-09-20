class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or len(matrix) == 0: return False
        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = m * n - 1
        while left <= right:
            mid = left + (right - left) /2
            x = mid / n
            y = mid % n
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

if __name__ == '__main__':
    solu = Solution()
    matrix = [[-10,-8,-6,-4,-3],[0,2,3,4,5],[8,9,10,10,12]]
    target = 0
    print solu.searchMatrix(matrix, target)
