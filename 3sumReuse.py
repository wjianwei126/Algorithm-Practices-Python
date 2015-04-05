# 3 sum, each number can be used more than 1 time
# e.g. input [0, -1, 2] ouput [0,0,0]

class Solution:
    def threeSum(self, num):
        if not num or len(num) < 3: return []
        re = []
        num.sort()
        for i in range(len(num)):
            if i > 0 and num[i] == num[i-1]:
                continue
            left = i
            right = len(num) - 1
            while left <= right:
                if num[i] + num[left] + num[right] == 0:
                    re.append([num[i], num[left], num[right]])
                    left += 1
                    while left <= right and num[left] == num[left-1]:
                        left += 1
                    right -= 1
                    while left <= right and num[right] == num[right+1]:
                        right -= 1
                elif num[i] + num[left] + num[right] > 0:
                    right -= 1
                    while left <= right and num[right] == num[right+1]:
                        right -= 1
                else:
                    left += 1
                    while left <= right and num[left] == num[left-1]:
                        left += 1
        return re

if __name__ == "__main__":
    solu = Solution()
    num = [-1, 0, 1, 2, -1, -4]
    print solu.threeSum(num)