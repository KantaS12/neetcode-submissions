class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_nums = set(nums.copy())

        if (len(set_nums) < len(nums)):
            return True

        return False
        