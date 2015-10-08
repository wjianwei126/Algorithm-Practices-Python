class Solution:
    def integerToEnglish(self, number):
        dic = {1: 'One', 2: 'Two', 3: "Three", 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', \
                 10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15:'Fifteen', 16: 'Sixteen', \
                 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty', \
                 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety'}
        res = ''

        three = number / 100
        if three > 0:
            res = str(dic[three]) + ' ' + 'Hundred' + ' '

        one = number % 10
        two = number % 100 - one

        if two == 0:
            if one > 0:
                res += str(dic[one])
            return res

        if two == 10:
            res += str(dic[one + two])
        else:
            if one > 0:
                res += str(dic[two]) + ' ' + str(dic[one])
            else:
                res += str(dic[two])

        return res

solution = Solution()
for i in [1,10,15,20,25,30,100,101,111,125,215]:
    print solution.integerToEnglish(i)
