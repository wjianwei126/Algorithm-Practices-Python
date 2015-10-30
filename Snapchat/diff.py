class Solution:
    def diff(self, s1, s2):
        M = len(s1)
        N = len(s2)
        dp = [[0] * (N+1) for x in range(M+1)]
        for i in range(M-1, -1, -1):
            for j in range(N-1, -1, -1):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        i = j = 0
        while i < M and j < N:
            if s1[i] == s2[j]:
                print '  ' + s1[i]
                i += 1
                j += 1
            elif dp[i+1][j] >= dp[i][j+1]:
                print '+ ' + s1[i]
                i += 1
            else:
                print '- ' + s2[j]
                j += 1

        while i < M or j < N:
            if i == M:
                print '- ' + s2[j]
                j += 1
            elif j == N:
                print '+ ' + s1[i]
                i += 1

solution = Solution()
s1 = ["#include<iostream>", "using namespace std;", \
    "void main() {", "    cout << 'Hello World!' << endl;", "}"]
s2 = ["#include<iostream>", "using namespace std;", \
    "void main() {", "    cout << 'Hello Snapchat!' << endl;", "}"]
solution.diff(s1, s2)
