# you can buy and sell as many times as you want, if you sell the stock today, you can not buy it tomorrow.
class Solution:
    def buyAndSellStock(self, prices):
        if not prices or len(prices) == 1: return 0
        unhold = [0] * len(prices) # the list represents the benefits we can get if we do not have stocks at the i th day
        hold = [-prices[0]] * len(prices) # the list represents the benefits we can get if we have stocks at the i th day
        for i in range(1, len(prices)):
            unhold[i] = max(unhold[i-1], hold[i-1] + prices[i])
            if i == 1:
                hold[i] = max(hold[0], 0-prices[1])
            else:
                hold[i] = max(hold[i-1], unhold[i-2] - prices[i])
        return unhold[-1]

solu = Solution()
prices = [1,2,3,4,1,3,2,5]
print solu.buyAndSellStock(prices)
