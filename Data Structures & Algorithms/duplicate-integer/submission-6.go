func hasDuplicate(nums []int) bool {
    var set = make(map[int]struct{})
    for _, num := range nums {
        _, exists := set[num]
        if exists{
            return true
        }
        set[num] = struct{}{}
    }
    return false
}
