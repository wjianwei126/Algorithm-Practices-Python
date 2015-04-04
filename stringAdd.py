# add two string, no sign, low digit is at the right side
# e.g. input: str1 = "001001", str2 = "001", output = "001010"

class Solution:

	def stringAddSimple(self, str1, str2):
		if not str1 or len(str1) == 0: return str2
		if not str2 or len(str2) == 0: return str1
		i = len(str1) - 1
		j = len(str2) - 1
		carry = 0
		output = ""
		while i >= 0 or j >= 0 or carry >0:
			if i < 0:
				num1 = 0
			else:
				num1 = int(str1[i])
			if j < 0:
				num2 = 0
			else:
				num2 = int(str2[j])

			sum = (num1 + num2 + carry) % 2
			carry = (num1 + num2 + carry) / 2

			output = str(sum) + output

			i -= 1
			j -= 1

		return output


if __name__ == "__main__":
	solu = Solution()
	str1 = "111011010"
	str2 = "1110010"

	print solu.stringAddSimple(str1, str2)
