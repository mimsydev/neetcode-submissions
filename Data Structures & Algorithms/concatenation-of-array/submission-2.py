class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        arr_len = len(nums)
        new_num_arr = [0] * len(nums) * 2
        for i, num in enumerate(nums):
            new_num_arr[i] = new_num_arr[i + arr_len] = nums[i]
        return new_num_arr