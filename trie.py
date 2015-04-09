# implement a trie

class Trie:
	def __init__ (self, words):
		self.root = {}
		for word in words:
			cur_dict = self.root
			for letter in word:
				cur_dict = cur_dict.setdefault(letter, {})
			cur_dict = cur_dict.setdefault("_end_", "_end_")

	def inTrie(self, word):
		cur_dict = self.root
		for letter in word:
			if letter in cur_dict:
				cur_dict = cur_dict[letter]
			else:
				return False
		if "_end_" in cur_dict:
			return True
		else:
			return False

	def add(self, word):
		cur_dict = self.root
		for letter in word:
			cur_dict = cur_dict.setdefault(letter, {})
		cur_dict = cur_dict.setdefault("_end_", "_end_")

	def remove(self, word):
		cur_dict = self.root
		stack = []
		for letter in word:
			if letter in cur_dict:
				stack.append(cur_dict)
				cur_dict = cur_dict[letter]
			else:
				return   # word does not exist
		if "_end_" not in cur_dict:
			return       # word does not exist
		else:
			del cur_dict["_end_"]
		cur_dict = stack.pop()
		while len(cur_dict.keys()) == 1:
			cur_dict.clear()
			cur_dict = stack.pop()
		for key in cur_dict.keys():
			if cur_dict[key] == {}:
				del cur_dict[key]
				break




if __name__ == "__main__":
	trie = Trie(["foo", "bar", "barz", "baz"])
	print trie.root
	trie.add("fok")
	print trie.root
	trie.remove("bar")
	print trie.root
	trie.remove("baz")
	print trie.root
	#print trie.inTrie("bar")