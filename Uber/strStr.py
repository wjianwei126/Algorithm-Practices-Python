class Solution(object):
    def strStr(self, haystack, needle):
        # O(mn)
        if not needle: return 0
        if not haystack or len(haystack) < len(needle): return -1
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i] == needle[0]:
                found = True
                for j in range(len(needle)):
                    if needle[j] != haystack[i+j]:
                        found = False
                        break
                if found:
                    return i
        return -1

    def KMP(self, haystack, needle):
        if not needle: return 0
        if not haystack or len(haystack) < len(needle): return -1
        table = [0] * len(needle)
        i, j = 0, 1
        while j < len(needle):
            if needle[j] == needle[i]:
                table[j] = i + 1
                i += 1
                j += 1
            elif i > 0:
                i = table[i-1]
            else:
                table[j] = 0
                j += 1
        m = i = 0
        while m < len(haystack) - len(needle) + 1:
            if haystack[m+i] == needle[i]:
                i += 1
                if i == len(needle):
                    return m
            else:
                if i == 0:
                    m += 1
                else:
                    m = m + i - table[i-1]
                    i = table[i-1]
        return -1
solution = Solution()
haystack = 'helloworld'
needle = ''
haystack = ''
needle = ''
haystack = ''
needle = 'hello'
haystack = 'helloworld'
needle = 'oworl'
haystack = 'helloworld'
needle = 'sdaf'
haystack = 'helloworld'
needle = 'helloworlhellow'
print solution.strStr(haystack, needle)
print solution.KMP(haystack, needle)
