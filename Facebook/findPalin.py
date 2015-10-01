# Given a string list, find all pairs of strings which can be combined to be a palindrome. 
# eg: cigar + tragic -> cigartragic, none + xenon -> nonexenon

class Solution:
    def findPalin(self, strings):
        if not strings or len(strings) == 0: return ""
        _dict = {}
        for i in range(len(strings)):
            _dict[strings[i]] = i
        re = []
        for str in strings:
            for i in range(len(str)):
                if str[0:i+1] == str[0:i+1][::-1] and str[i+1:][::-1] in _dict:
                    re.append((str, strings[_dict[str[i+1:][::-1]]]))
        
        return re
        
	
if __name__ == "__main__":
    strings = ["cigar", "tragic", "none", "xenon", "book"]
    
    solu = Solution()
    print solu.findPalin(strings)