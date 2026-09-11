func groupAnagrams(strs []string) [][]string {
	wordMap := make(map[[26]uint8][]string)
	retSlice := make([][]string,0)

	for _, word := range strs {
		var charCountSlice [26]uint8
		for _, char := range []byte(word){
			charCountSlice[char - 'a']++
		}
		_, ok := wordMap[charCountSlice]; if ok {
			wordMap[charCountSlice] = append(wordMap[charCountSlice], word)
		} else {
			wordMap[charCountSlice] = []string{word}
		}
	}

	for _, wordSlice := range wordMap {
		retSlice = append(retSlice, wordSlice)
	}
	return retSlice
}
