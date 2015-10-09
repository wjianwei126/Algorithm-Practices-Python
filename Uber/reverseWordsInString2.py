class Solution:
    def reverseWord(self, s):
        if not s: return
        self.s = s
        self.reverse(0, len(s)-1)
        start = 0
        for i in range(len(s)):
            if self.s[i] == ' ':
                self.reverse(start, i-1)
                start = i+1

        return self.s

    def reverse(self, start, end):
        s = list(self.s)
        while start <= end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        self.s = ''.join(s)

solution = Solution()
s = 'I love you'
print solution.reverseWord(s)
