class Solution:
    def climbStairs(self, n: int) -> int:

        # This is for bottom-up programming O(1) space O(n) time
        if n <= 2:
            return n
        
        two_before = 1
        one_before = 2

        for i in range(3, n+1):
            # Since we know that it goes from 0, 1, 2 ... since it's 1 to 2 steps

            two_before, one_before = one_before, one_before + two_before

        return one_before

