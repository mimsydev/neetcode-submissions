class Solution:
	def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
		ret_list: List[List[str]] = [[]]
		word_map: dict[tuple[int,...],List[str]] = {}
		for word in strs:
			alphabet_arr = [0] * 26
			for i, char in enumerate(word):
				alphabet_arr[ord(char)-ord('a')] += 1
			tuple_key = tuple(alphabet_arr)
			if tuple_key in word_map:
				word_map[tuple_key].append(word)
			else:
				word_map[tuple_key] = [word]
		ret_list = list(word_map.values())
		return ret_list
		
