class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        i = m - 1
        j = n - 1
        pos = m + n - 1
        while pos >= 0:
            if i < 0 or (j >= 0 and nums2[j] >= nums1[i]):
                nums1[pos] = nums2[j]
                j -= 1
                pos -= 1
            else:
                nums1[pos] = nums1[i]
                i -= 1
                pos -= 1

solu = Solution()
nums1 = [0]
m = 0
nums2 = [1]
n = 1
solu.merge(nums1, m, nums2, n)
print nums1
