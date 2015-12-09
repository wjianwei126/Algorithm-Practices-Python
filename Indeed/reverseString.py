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

def reverseHTMLStringBetter(s):
    if not s: return ''
    arr = list(s)
    res = []
    dic = {}
    swap(arr, 0, len(arr) - 1)

    start = -1
    for i in range(len(arr)):
        if arr[i] == ';':
            start = i
        if arr[i] == '&' and start != -1:
            dic[start] = i
            start = -1

    for key in dic.keys():
        swap(arr, key, dic[key])

    return ''.join(arr)

def swap(nums, beg, end):
    while beg < end:
        nums[beg], nums[end] = nums[end], nums[beg]
        beg += 1
        end -= 1

s = '1234&euro;'
s = '1234&euro'
s = '1234&euro;567'
s = '12345&78&amp;888'
s = '&&&&&'
print reverseHTMLStringBetter(s)
