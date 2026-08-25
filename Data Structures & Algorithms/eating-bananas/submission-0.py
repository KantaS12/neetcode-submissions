import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # So my idea is that 'h' is a really important number here. It actually just dictates what the rate is already. (I.E.) if len(piles) == h then the k needs to be the max(piles) since we need to eat it all in an hour per pile.

        # Since we found our upper bound and now we need to find the lower bound. The lower bound is actually 1 because that's the least they could eat per hr. 

        # So since we found it we could make an hypothetical and use a binary search to go left and right and say if it eats too slow or less than h then we move left up 1 and if it eats too fast then we move right with mid.


        left = 1
        right = max(piles)

        result = right 

        while left <= right:

            mid = (left + right) // 2
            
            total_hours = 0

            for pile in piles:
                total_hours += math.ceil(pile / mid)

            if total_hours <= h:
                result = mid
                right = mid - 1

            elif total_hours > h:
                # too slow
                left = mid + 1

        return result

