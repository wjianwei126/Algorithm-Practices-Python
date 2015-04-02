# 0-1 knapsack problem

class Solution:
	def maxValue(self, gold, silver, maxWeight):
		weight = gold + silver
		length = len(gold) + len(silver)
		price = []
		for x in range(length):
			if x < len(gold):
				price.append(10*gold[x])
			else:
				price.append(1*silver[x-len(gold)])
	
		#print weight
		#print price

		value = [[0] * (length + 1)  for x in range(maxWeight + 1)]
		#print value

		for w in range(1, maxWeight + 1):
			for j in range(length):
				if weight[j] > w:
					value[w][j+1] = value[w][j]
				else:
					value[w][j+1] = max(value[w][j], price[j] + value[w-weight[j]][j])

		#print value
		return value[maxWeight][length]


if __name__ == "__main__":
	solu = Solution()
	print solu.maxValue([9000,100,10,1],[1000,900,90],10000)