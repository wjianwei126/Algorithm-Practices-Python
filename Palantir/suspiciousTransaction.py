def findSuspicious(records):
    dic = {}
    suspicious = {}
    for name, amount, city, time in records:
        if amount > 3000:
            if name not in suspicious:
                suspicious[name] = set()
            suspicious[name].add(time)

        if name in dic:
            for timePoint, cityPlace in dic[name]:
                if abs(timePoint - time) <= 60 and city != cityPlace:
                    if name not in suspicious:
                        suspicious[name] = set()
                    suspicious[name].add(time)
                    suspicious[name].add(timePoint)
            dic[name].append((time, city))
        else:
            dic[name] = [(time, city)]

    print dic
    print suspicious

    susList = []
    for name in suspicious:
        susList.append((name, min(suspicious[name])))

    print susList

    susList.sort(key=lambda x:x[1])

    print susList

    res = []
    for name, time in susList:
        res.append(name)

    print res

records = [('Kevin', 423, 'A', 823), \
           ('Kevin', 520, 'B', 871), \
           ('Doggy', 4000, 'A', 53), \
           ('Bob', 23, 'C', 783), \
           ('Ali', 4, 'A', 344), \
           ('Vanit', 312, 'D', 230), \
           ('Ali', 12, 'A', 300), \
           ('Kevin', 3001, 'F', 420), \
           ('Kevin', 1, 'K', 20), \
           ('Elen', 500, 'G', 621)]

findSuspicious(records)
