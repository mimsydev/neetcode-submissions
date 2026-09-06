class Solution:

    def hasDuplicate(self, nums: List[int]) -> bool:
        j: set(int) = set()
        for n in nums:
            if n in j:
                return True
            j.add(n)
        return False


        