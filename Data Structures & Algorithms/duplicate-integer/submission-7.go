func hasDuplicate(nums []int) bool {
    numSet := make(map[int]struct{})
    for _, num := range nums {
        _, ok := numSet[num]; if ok {
            return true
        }
        numSet[num] = struct{}{}
    }
    return false
}
