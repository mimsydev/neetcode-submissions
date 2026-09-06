class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map: dict = {}
        for ind, val in enumerate(nums):
            diff = target - val
            if diff in num_map:
                return [num_map[diff], ind]
            num_map[val] = ind
