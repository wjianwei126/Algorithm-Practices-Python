import heapq
class Solution:
    def rearrangeList(self, s):
        if not s or len(s) == 1: return s
        dic = {}
        for ch in s:
            dic[ch] = dic.get(ch, 0) + 1
            if dic[ch] > (len(s) + 1) / 2:
                return ''
        heap = []
        # O(nlogn)
        for ch in dic:
            heapq.heappush(heap, (-dic[ch], ch))
        res = ''
        while heap:
            count, ch = heapq.heappop(heap)
            if not res or res[-1] != ch:
                res += ch
                count += 1
                if count != 0:
                    heapq.heappush(heap, (count, ch))
            else:
                # if not heap:
                #     return ''
                count2, ch2 = heapq.heappop(heap)
                res += ch2
                count2 += 1
                if count2 != 0:
                    heapq.heappush(heap, (count2, ch2))
                heapq.heappush(heap, (count, ch))
        return res

solution = Solution()
s = 'aabaaabbc'
print solution.rearrangeList(s)
