func getConcatenation(nums []int) []int {
    leng := len(nums)
    retNums := make([]int, leng * 2)
    for i:=0; i<leng; i++ {
        num := nums[i]
        retNums[i] = num
        retNums[i + leng] = num
    }

    return retNums
}
