class Solution(object):
    def wordBreak(self, s, wordDict):
        maxLen = 0
        minLen = 0
        for ele in wordDict:
            maxLen = max(len(ele), maxLen)
            minLen = min(len(ele), minLen)
        dp = [[] for _ in xrange(len(s)+1)] # store the valid setence end at mark i
        #initialize start from minLen, maxLen
        if len(s) < minLen:
            return []
        for right in xrange(minLen,len(dp)):
            for left in xrange(max(0,right-maxLen), right-minLen):
                if left == 0 and s[left:right] in wordDict:
                    dp[right].append(left)

                elif len(dp[left]) > 0 and s[left:right] in wordDict:
                    dp[right].append(left)
                    
        #reverse
        if len(dp[-1]) == 0:
            return []
        rel = []
        tmp = self.combine(s, dp, len(dp)-1)

        for ele in tmp:
            rel.append(" ".join(ele))
        return rel

    def combine(self, s, dp, right):
        tmp = []
        for left in dp[right][::-1]:
            if left == 0:
                tmp.append([s[left:right]])
            else:
                tmp_next = self.combine(s, dp, left)
                for ele in tmp_next:
                    ele.append(s[left:right])
                    tmp.append(ele)


        return tmp

if __name__ == '__main__':
    solu = Solution()
    s = 'catsanddog'
    wordDict = set(["cat", "cats", "and", "sand", "dog"])
    print solu.wordBreak(s, wordDict)
