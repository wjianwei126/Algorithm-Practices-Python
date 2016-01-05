def coinCombination(V, k):
    if k < 0 or V <= 0:
        raise ValueError('The input is invalid')

    combination = []
    while V > 0:
        if V >= 2 ** k:
            combination.append(2**k)
            V -= 2 ** k
        else:
            k -= 1
    return combination

for v in range(1, 100):
    print v, coinCombination(v, 5)
