import heapq
import random
class Solution:
	def topK1(self, S, k):
		"O(nlogn)"
		if not S or len(S) == 0 or k <= 0: return []
		if k >= len(S): return S
		S.sort()
		re = []
		for i in range(k):
			re.append(S[len(S)-1-i])
		return re

	def topK2(self, S, k):
		"O(n*k)"
		if not S or len(S) == 0 or k <= 0: return []
		if k >= len(S): return S
		for i in range(k):
			for j in range(len(S)-i-1):
				if S[i] > S[i+1]:
					S[i], S[i+1] = S[i+1], S[i]
		re = []
		for i in range(k):
			re.append(S[len(S)-1-i])
		return re

	def topK3(self, S, k):
		"O(nlogk)"
		if not S or len(S) == 0 or k <= 0: return []
		if k >= len(S): return S

		heap = []
		for i in range(k):
			heapq.heappush(heap, S[i])

		for i in range(k, len(S)):
			if heap[0] < S[i]:
				heapq.heappop(heap)
				heapq.heappush(heap, S[i])

		re = []
		for i in range(k):
			re.append(heapq.heappop(heap))
		return re

	def topK4(self, S, k):
		"O(n)"
		if not S or len(S) == 0 or k <= 0: return []
		if k >= len(S): return S
		
		def findK(input, k):
			if k <= 0:
				return []
			if len(input) <= k:
				return input
			(Sa, Sb) = partition(input)

			return findK(Sa, k) + findK(Sb, k- len(Sa))

		def partition(input):
			Sa = []
			Sb = []
			index = random.randrange(len(input))
			input[0], input[index] = input[index], input[0]
			pivot = input[0]
			for i in range(1, len(input)):
				if input[i] > pivot:
					Sa.append(input[i])
				else:
					Sb.append(input[i])
			if len(Sa) < len(Sb):
				Sa.append(input[0])
			else:
				Sb.append(input[0])

			return (Sa, Sb)

		return findK(S,k)





if __name__ == "__main__":
	solu = Solution()
	S = [3,1,4,5,23,65,87,1,0,-1,23,21,45,666]
	print solu.topK1(S, 5)
	print solu.topK2(S, 5)
	print solu.topK3(S, 5)
	print solu.topK4(S, 5)