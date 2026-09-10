func getConcatenation(nums []int) []int {
    var ans = make([]int, len(nums) * 2)
    for i, num := range nums{
        ans[i] = num
        ans[i + len(nums)] = num
    }
    return ans
}
