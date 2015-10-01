# Maximum size square sub-matrix with all 1s

class Solution:
    def maxOneSquare(self, map):
        if not map or len(map) == 0 or len(map[0]) == 0: return 0
        m = len(map)
        n = len(map[0])
        dp = [[0] * n for x in range(m)]
        for i in range(m):
            dp[i][0] = map[i][0]
        for j in range(n):
            dp[0][j] = map[0][j]
            
        for i in range(1, m):
            for j in range(1, n):
                if map[i][j] == 1:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                else:
                    dp[i][j] = 0
        
        maxsofar = 0
        for i in range(m):
            for j in range(n):
                maxsofar = max(maxsofar, dp[i][j])
                
        return maxsofar
        

if __name__ == "__main__":
    solu = Solution()
    A = [[1,1,0,1,0], [0,1,1,1,1], [0,1,1,1,1], [0,1,1,1,0], [1,0,1,1,1]]
    print solu.maxOneSquare(A)