class Solution:
	def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
		word_dict: dict[tuple[str,...],List[str]] = {}
		for word in strs:
			tuple_key = tuple(sorted(word))
			if tuple_key not in word_dict:
				word_dict[tuple_key] = []
			word_dict[tuple_key].append(word)
		return list(word_dict.values())

        