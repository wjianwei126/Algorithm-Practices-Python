class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        # Time O(n^2), Space O(n)
        if not ratings: return 0
        candy = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candy[i] = candy[i-1] + 1
            else:
                if candy[i-1] == 1:
                    j = i - 1
                    while j >= 0 and ratings[j] > ratings[j+1] and candy[j] == candy[j+1]:
                        candy[j] += 1
                        j -= 1
        return sum(candy)

    def candy2(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        # Time O(n), Space O(n)
        if not ratings: return 0
        candy = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candy[i] = candy[i-1] + 1
        res = candy[-1]
        for j in range(len(ratings)-1)[::-1]:
            if ratings[j] > ratings[j+1] and candy[j] <= candy[j+1]:
                candy[j] = candy[j+1] + 1
            res += candy[j]
        return res

if __name__ == '__main__':
    solu = Solution()
    ratings = [4, 5, 4, 3, 7, 6, 1, 2]
    print solu.candy(ratings)
