class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)

        result, current = [], []

        def backtrack(i):

            # base case (if the index is at the end of the array)
            if i == n:
                result.append(current[:]) # We want to get the snap shot of the current
                return

            # We don't take nums[i]
            backtrack(i + 1)

            # We take nums[i]
            current.append(nums[i])
            backtrack(i + 1)
            current.pop()

        backtrack(0)
        return result
        