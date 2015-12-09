def findWordBeforeK(s, k):
    if not s: return []
    if k > len(s) - 1:
        return s.split(' ')
    res = []
    temp = ''
    i = 0
    while i <= k:
        if s[i] == ' ':
            res.append(temp)
            temp = ''
        else:
            temp += s[i]
        i += 1
    return res

s = 'abc def gh i'
print findWordBeforeK(s, 3)
print findWordBeforeK(s, 5)
print findWordBeforeK(s, 9)
print findWordBeforeK(s, 11)
print findWordBeforeK(s, 12)
