def sortByTimesAndIndex(inputList):
    if not inputList: return []
    dic = {}
    for i in range(len(inputList)):
        if inputList[i] not in dic:
            dic[inputList[i]] = [i]
        else:
            dic[inputList[i]].append(i)
    keyList = dic.keys()
    keyList.sort(key=lambda x:-len(dic[x]))
    res = []
    for key in keyList:
        for element in dic[key]:
            res.append((key, element))
    return res

inputList = ['a', 'c', 'a', 'a', 'b', 'd', 'c', 'c', 'a', 'b']
print sortByTimesAndIndex(inputList)
