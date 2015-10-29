# leftpass of an element x is defined as the number of elements on left side of x which is larger than element x. find the maximum leftpass of an array
import heapq
class Solution:
    def bruteForce(self, nums):
        # O(n^2)
        if not nums or len(nums) == 1: return 0
        # res = 0
        res = [0]
        for i in range(1, len(nums)):
            count = 0
            for j in range(i):
                if nums[j] > nums[i]:
                    count += 1
            # res = max(count, res)
            res.append(count)
        return res

    def mergeSortMethod(self, nums):
        # O(nlogn)
        if not nums or len(nums) == 1: return 0
        sp = [0] * len(nums)
        vp = []
        for i in range(len(nums)):
            vp.append((nums[i], i))
        self.mergeSort(vp, sp)
        res = 0
        for n in sp:
            res = max(res, n)
        return res

    def mergeSort(self, vp, sp):
        if len(vp) < 2: return
        mid = len(vp) / 2
        va = vp[:mid]
        vb = vp[mid:]
        self.mergeSort(va, sp)
        self.mergeSort(vb, sp)
        left = right = pointer = 0
        while left < len(va) or right < len(vb):
            if left < len(va) and right < len(vb):
                if va[left][0] > vb[right][0]:
                    vp[pointer] = va[left]
                    pointer += 1
                    left += 1
                else:
                    id = vb[right][1]
                    sp[id] += left
                    vp[pointer] = vb[right]
                    pointer += 1
                    right += 1
            elif left < len(va):
                vp[pointer] = va[left]
                pointer += 1
                left += 1
            else:
                id = vb[right][1]
                sp[id] += left
                vp[pointer] = vb[right]
                pointer += 1
                right += 1

    def heapMethod(self, nums):
        # O(nlogn) time
        if not nums or len(nums) == 1: return []
        heap = []
        res = [0]
        heapq.heappush(heap, nums[0])
        for i in range(1, len(nums)):
            if nums[i] < heap[0]:
                print nums[i]
                res.append(len(heap))
                heapq.heappush(heap, nums[i])
            else:
                temp = []
                while heap and heap[0] <= nums[i]:
                    temp.append(heapq.heappop(heap))
                res.append(len(heap))
                for num in temp:
                    heapq.heappush(heap, num)
                heapq.heappush(heap, nums[i])
        return res

solu = Solution()
# nums = [5,3,4,2,7,1,6]
# print solu.bruteForce(nums)
# print solu.mergeSortMethod(nums)
nums = [3,1,2,9,5,4,3]
print solu.heapMethod(nums)
