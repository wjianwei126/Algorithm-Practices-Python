import random
class Solution:
    def selectKItems(self, stream, k):
        candidates = [0] * k
        for i in range(k):
            candidates[i] = stream[i]

        for i in range(k+1, len(stream)):
            j = random.randint(0, i)
            if j < k:
                candidates[j] = stream[i]
