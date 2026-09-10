func isAnagram(s string, t string) bool {
    if len(s) != len(t) {
        return false
    }

    var sMap = make(map[rune]int)
    var tMap = make(map[rune]int)

    for _, char := range s {
        sMap[char]++
    }
    for _, char := range t {
        tMap[char]++
    }

    for _,char := range t {
        sCount, ok := sMap[char]; if !ok {
            return false
        }
        if sCount != tMap[char] {
            return false
        }
    }

    return true
}
