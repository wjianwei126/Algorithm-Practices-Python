class Solution:
    def encodeString(self, s):
        if not s: return ''
        if len(s) == 1: return s
        res = ''
        i = 0
        while i < len(s):
            if ord(s[i]) >= ord('0') and ord(s[i]) <= ord('9'):
                count = 1
                num = s[i]
                while i + 1 < len(s) and s[i+1] == s[i]:
                    i += 1
                    count += 1
                res += str(count) + 'x' + str(num)
            else:
                if i + 1 < len(s) and s[i+1] == s[i]:
                    count = 1
                    char = s[i]
                    while i + 1 < len(s) and s[i+1] == s[i]:
                        i += 1
                        count += 1
                    res += str(count) + 'x' + str(char)
                else:
                    res += s[i]
            i += 1
        return res

    def decodeString(self, s):
        if not s: return ''
        if len(s) == 1: return s
        res = ''
        i = 0
        temp = 0
        while i < len(s):
            if ord(s[i]) >= ord('0') and ord(s[i]) <= ord('9'):
                temp = temp * 10 + int(s[i])
                i += 1
                while ord(s[i]) >= ord('0') and ord(s[i]) <= ord('9'):
                    temp = temp * 10 + int(s[i])
                    i += 1
            elif s[i] == 'x' and temp > 0:
                i += 1
                res += temp * s[i]
                temp = 0
                i += 1
            else:
                res += s[i]
                i += 1
        return res

solution = Solution()
s = 'abc2ddddefg'
# s = 'abc5xefg'
# s = '1111111'
# s = 'aaaaa'
# s = '3g2rg2'
# s = 'abc55555xefg'
encode = solution.encodeString(s)
print encode
decode = solution.decodeString(encode)
print decode
