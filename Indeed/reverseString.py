def reverseString(s):
    if not s: return ''
    res = ''
    i = len(s) - 1
    while i >= 0:
        res += s[i]
        i -= 1
    return res

def reverseHTMLString(s):
    if not s: return ''
    res = []
    temp = ''
    i = 0
    while i < len(s):
        if s[i] == '&':
            res.append(reverseString(temp))
            temp = '&'
        elif s[i] == ';':
            res.append(temp + ';')
            temp = ''
        else:
            temp += s[i]
        i += 1
    if temp != '':
        res.append(reverseString(temp))
    return ''.join(res[::-1])

s = '1234&euro;'
s = '1234&euro'
s = '1234&euro;567'
print reverseHTMLString(s)
