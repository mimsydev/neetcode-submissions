func getConcatenation(nums []int) []int {
    leng := len(nums)
    retNums := make([]int, leng * 2)
    for i, num := range nums{
        retNums[i] = num
        retNums[i + leng] = num
    }

    return retNums
}
