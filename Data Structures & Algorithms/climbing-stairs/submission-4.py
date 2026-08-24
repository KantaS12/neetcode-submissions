class Solution:
    def climbStairs(self, n: int) -> int:

        # Basically DP programming again
        # * Move 1 or 2
        # output is the amount of ways
        # Let's actually keep track of our options?

        # Let's actually keep by making a memo
        memo = {} # Key: 1 and 2 Value: Amount of ways from there?

        def dfs(curr):

            # Let's check if it's in our memory already 
            if curr in memo:
                return memo[curr]

            # If you reach n how many ways?
            if curr == n:
                return 1

            # If you're past the end
            if curr > n:
                return 0 # Failed path

            memo[curr] = dfs(curr + 1) + dfs(curr + 2)

            return memo[curr]
        
        return dfs(0)
        