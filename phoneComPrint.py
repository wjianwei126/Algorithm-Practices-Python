# phone letter combination print directly

class Solution:
    # @return a list of strings, [s1, s2]
    _dict = {2:["a","b","c"], 3:["d","e","f"], 4:["g","h","i"], 5:["j","k","l"], 6:["m","n","o"], 7:["p","q","r","s"], \
            8:["t", "u", "v"], 9:["w", "x", "y", "z"]}
    def letterCombinations(self, digits):
    	self.letterComb(digits, "")
    def letterComb(self, digits, prev):
    	if not digits: 
        	print prev
    	else:
        	for letter in self._dict[int(digits[0])]:
        		self.letterComb(digits[1:], prev + letter)



if __name__ == "__main__":
	solu = Solution()
	digits = "234"
	solu.letterCombinations(digits)