func getConcatenation(nums []int) []int {
    l := len(nums)
    n := make([]int, l * 2)
    for i:=0; i<l; i++ {
        n[i] = nums[i]
        n[i + l] = nums[i]
    }

    return n
}
