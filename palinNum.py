# find the number of palindromic substrings in a given string
# e.g. aba => 4  abba => 6

class Solution:
    def palinNum(self, str):
        if not str or len(str) == 0: return 0
        count = 0
        for i in range(len(str)):
            # odd
            l = r = i
            while l >= 0 and r < len(str) and str[l] == str[r]:
                count += 1
                l -= 1
                r += 1
            # even
            l = i
            r = i + 1
            while l >= 0 and r < len(str) and str[l] == str[r]:
                count += 1
                l -= 1
                r += 1
        
        return count

	   

if __name__ == "__main__":
    str1 = "aobboa"
    solu = Solution()
    print solu.palinNum(str1)