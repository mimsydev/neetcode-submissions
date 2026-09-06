class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = [0] * (2 * length)
        for ind, num in enumerate(nums):
            ans[ind] = ans[ind+length] = num
        return ans