# Implement a method called printNonComments() 
# which prints out a extract of text with comments removed. 

# For example, the input: 

# hello /* this is a 
# multi line comment */ all 

# Should produce: 

# hello 
# all 

# You have access to a method called getNextLine() which returns the next line in the input string.
class Solution():
	def removeComments(self):
		"this method can not deal with */ and /* that is seperated as / and * in two lines"


		text = open("test.txt")
		output = ""
		flag = False
		while True:
			line = text.readline()
			if not line:
				break
			i = 0
			while i < len(line):
				if line[i] not in ["/", "*"]:
					if not flag:
						output += line[i]
					i += 1
				elif line[i] == "/":
					if i < len(line) - 2 and line[i+1] == "*" and line[i+2] != "/":
						flag = True
						i += 2
					elif i < len(line) - 2 and line[i+1] == "*" and line[i+2] == "/":
						if flag:
							output += line[i]
							flag = False
							i += 3
						else:
							flag = True
							output += line[i+2]
							i += 3
					elif i == len(line) - 2 and line[i+1] == "*":
						flag = True
						i += 2
					else:
						if not flag:
							output += line[i]
						i += 1
				elif line[i] == "*":
					if i < len(line) - 1 and line[i+1] == "/":
						if flag:
							flag = False
							i += 2
						else:
							output += line[i] + line[i+1]
							i += 2
					else:
						if not flag:
							output += line[i]
						i += 1
		print output

if __name__ == "__main__":
	solu = Solution()
	solu.removeComments()


					


			

