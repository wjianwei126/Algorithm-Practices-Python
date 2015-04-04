# imitate cd
# Given an original path and a cd command, output the final path
# e.g. input: /home/kevin  fun/download/../  output: /home/kevin/fun

class Solution:
	def imitateCD(self, inputStr, cdCommand):
	    inputStr = inputStr.split("/")
	    stack = []
	    for item in inputStr:
	    	if item not in ["", ".", "/"]:
	        	stack.append(item)
	    cdCommand = cdCommand.split("/")
	    for item in cdCommand:
	        if item in ["", ".", "/"]:
	            continue
	        elif item  == "..":
	            if stack:
	                stack.pop()
	            else:
	                continue
	        else:
	            stack.append(item)
	   
	    return "/" + "/".join(stack) if stack else "/"

if __name__ == "__main__":
    input = "/home/kevin"
    cd = "fun/download/../../../"
    solu = Solution()
    print solu.imitateCD(input, cd)