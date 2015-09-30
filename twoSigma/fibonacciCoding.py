import unittest
class Solution(unittest.TestCase):
    def encode(self, n):
        if n <= 0: return -1
        if n == 1: return '1'
        fibonacci = [1, 2]
        i = 1
        while fibonacci[i] <= n:
            fibonacci.append(fibonacci[i-1] + fibonacci[i])
            i += 1
        res = ''
        i -= 1
        while i >= 0:
            if fibonacci[i] <= n:
                res = '1' + res
                n -= fibonacci[i]
            else:
                res = '0' + res
            i -= 1
        return res

    def test(self):
        self.assertEqual(self.encode(0), -1)
        self.assertEqual(self.encode(1), '1')
        self.assertEqual(self.encode(12), '10101')
        self.assertEqual(self.encode(5), '0001')
        self.assertEqual(self.encode(4), '101')

if __name__ == '__main__':
    unittest.main()
