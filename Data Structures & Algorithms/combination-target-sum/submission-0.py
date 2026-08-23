class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
    
        n = len(nums)
        res = []
        def backtrack(i, arr, curr_sum):

            # Base cases
            # index >= n
            if i >= n:
                return # Stop

            # curr_sum == target
            if curr_sum == target:
                res.append(arr[:])
                return  # Stop

            # curr_sum > target
            elif curr_sum > target:
                return # Stop

            # Keep the index and go left
            backtrack(i, arr + [nums[i]], curr_sum + nums[i])

            # Move index up and then add current to array
            backtrack(i + 1, arr, curr_sum)

            # Note this is different from doing res, curr = [], []
            # You can also do that but you need to pop() and append tricks.

        backtrack(0, [], 0)

        return res