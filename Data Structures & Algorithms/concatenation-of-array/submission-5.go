func getConcatenation(nums []int) []int {
    leng := len(nums)
    retNums := make([]int, leng * 2)
    for i:=0; i<leng; i++ {
        retNums[i] = nums[i]
        retNums[i + leng] = nums[i]
    }

    return retNums
}
