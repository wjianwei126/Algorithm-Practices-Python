def cipher(s, k):
    if not s: return ''
    res = ''
    for ch in s:
        res +=  encode(ch, k)
    return res

def encode(ch, k):
    k = k % 26

    newASCII = ord(ch) + k
    if newASCII > ord('Z'):
        newASCII = newASCII - ord('Z') + ord('A') - 1
    return chr(newASCII)

print cipher('ABCDEFGHIJKLMNOPQRSTUVWXYZ', -26)
