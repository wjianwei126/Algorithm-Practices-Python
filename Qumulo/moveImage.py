class Solution:
    def moveImage(self, image, startX1, startY1, startX2, startY2, endX1, endY1, endX2, endY2):
        m = len(image)
        n = len(image[0])
        width = startY2 - startY1 + 1
        length = startX2 - startX1 + 1
        temp = [[0] * width for x in range(length)]
        for i in range(startX1, startX2 + 1):
            for j in range(startY1, startY2 + 1):
                temp[i-startX1][j-startY1] = image[i][j]

        for i in range(endX1, endX2 + 1):
            if i < 0 or i >= m:
                continue
            for j in range(endY1, endY2 + 1):
                if j < 0 or j >= n:
                    continue
                image[i][j] = temp[i-endX1][j-endY1]

        return image

image = [[0,1,2,3,4,5], \
         [6,7,8,9,10,11], \
         [12,13,14,15,16,17], \
         [18,19,20,21,22,23], \
         [24,25,26,27,28,29], \
         [30,31,32,33,34,35]]

solution = Solution()
# print solution.moveImage(image, 1,1,3,2,3,4,5,5)
# print solution.moveImage(image, 1,1,3,2,4,5,6,6)
print solution.moveImage(image, 1,1,3,2,2,2,4,3)
