class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ln = len(nums)
        ans: List[int] = [0] * ln * 2
        for i, num in enumerate(nums):
            ans[i] = ans[i + ln] = num

        return ans
        