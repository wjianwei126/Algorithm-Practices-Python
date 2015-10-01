# each number reprensents several letters, given a list of number, output all the possible letter combination
# e.g. input: {1:["A", "B"], 2:["C", "D", "E"]}  output: ["AC", "AD", "AE", "BC", "BD", "BE"]

class Solution:
	mydict = {}
	def translateNum(self, _dict, num):
	    if not _dict or not num or len(num) == 0: return []
	    self.mydict = _dict
	    return self.translator(num)
	    
	def translator(self, num):
	    if len(num) == 0: return []
	    re = [] 
	    
	    remain = self.translator(num[1:])
	    for letters in self.mydict[num[0]]:
	    	if remain:
	        	for items in remain:
	        		re.append(letters + items)
	        else:
	        	re.append(letters)
	    return re
	   

if __name__ == "__main__":
    input = {1:["A", "B"], 2:["C", "D", "E"]}
    num = [1,2,2]
    solu = Solution()
    print solu.translateNum(input, num)