# Given:
# int array of size k
# int N
# int a_init within [0, k)
# values in array within [0, k)
# A_0 = a_init
# A_1 = arr[A_0]
# A_2 = arr[A_1]
# ...
# A_i = arr[A_i-1]
# Find A_N.
class Solution:
    def bruteForce(self, nums, N, a_init):
        # O(N)
        if not nums: return None
        A = a_init
        for i in range(N):
            A = nums[A]

        return A

    def countinuousFinding(self, nums, N, a_init):
        # O(k)
        if not nums: return None
        occuredIndex = {}
        A = a_init
        occuredIndex[A] = 1

        cycleStart = None
        for i in range(1, N+1):
            A = nums[A]
            if A in occuredIndex:
                cycleStart = occuredIndex[A]
                break
            else:
                occuredIndex[A] = i + 1

        if not cycleStart:
            return A
        else:
            N = (N - cycleStart + 1) % (len(occuredIndex) - cycleStart + 1)

        A = a_init
        for i in range(cycleStart - 1 + N):
            A = nums[A]
        return A

solu = Solution()
nums = [7, 6, 8, 4, 5, 1, 3, 8, 1, 2]
N = 10
a_init = 7
print solu.bruteForce(nums, N, a_init)
print solu.countinuousFinding(nums, N, a_init)
