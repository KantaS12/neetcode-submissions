class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0 #idx 1 (for pt1)
        right = 1 #idx 2 (for pt2)

        # Find maximum profit
        max_profit = 0

        # If len(prices) == 1 return 0

        if len(prices) <= 1: # Constraint
            return 0

        # Go through array

        while right < len(prices):

            # While profitable
            if prices[right] > prices[left]:
                cal_total = prices[right] - prices[left] # Calculate profit

                if cal_total > max_profit:
                    max_profit = cal_total # Add to max profit

            # Not profitable
            elif prices[left] > prices[right]:
                # Move to the left pointer to the right pointer
                left = right
            
            right += 1

        if max_profit != 0:
            return max_profit

        return 0 