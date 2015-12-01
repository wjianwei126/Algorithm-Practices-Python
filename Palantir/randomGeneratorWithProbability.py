import random
class RandomGenerator:
    def __init__(self, probabilities):
        if sum(probabilities) != 1:
            raise ValueError('Invalid probabilities')
        self.distribution = []
        prob = 0
        for p in probabilities:
            prob += p
            self.distribution.append(prob)

    def generateNum(self):
        prob = random.random()
        for i in range(len(self.distribution)):
            if prob < self.distribution[i]:
                return i
        # left, right = 0, len(self.distribution) - 1
        # while left < right:
        #     mid = left + (right - left) / 2
        #     if self.distribution[mid] > prob:
        #         right = mid
        #     else:
        #         left = mid + 1
        # return left


probabilities = [0.2, 0.3, 0.5]
generator = RandomGenerator(probabilities)
print generator.distribution
out = {0:0, 1:0, 2:0}
for i in range(10000):
    rand = generator.generateNum()
    out[rand] += 1
print out
