class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s: return ''
        ss = s + '#' + s[::-1]
        print ss
        table = [0] * len(ss)
        i, j = 0, 1
        while j < len(ss):
            if ss[i] == ss[j]:
                table[j] = i + 1
                i += 1
                j += 1
            elif i > 0:
                i = table[i-1]
            else:
                table[j] = 0
                j += 1
        index = table[-1]
        print table
        return s[index:][::-1] + s

if __name__ == '__main__':
    solu = Solution()
    s = "abbabaab"
    print solu.shortestPalindrome(s)
