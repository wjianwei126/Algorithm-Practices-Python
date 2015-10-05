# djb2 algorithm to hash strings

def djb2(string):
    hash = 5381
    for i in range(len(string)):
        hash = hash * 33 ^ string[i]
        # hash = ((hash << 5) + hash) + stirng[i]
    return hash
