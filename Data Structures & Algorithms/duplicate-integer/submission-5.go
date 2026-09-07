func hasDuplicate(nums []int) bool {
    var set = make(map[int]bool)
    for _, num := range nums {
        _, exists := set[num]
        if exists{
            return true
        }
        set[num] = true
    }
    return false
}
