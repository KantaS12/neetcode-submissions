import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # Make a max heap
        max_heap = [-n for n in stones]

        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            # If you use heapq.heappop() then it takes the root
            heavy1 = heapq.heappop(max_heap) * -1
            heavy2 = heapq.heappop(max_heap) * -1

            if heavy1 == heavy2:
                continue

            newHeavy = heavy1 - heavy2
            heapq.heappush(max_heap, newHeavy * -1)

        # Base cases
        if len(max_heap) == 0:
            return 0

        if len(max_heap) == 1:
            return max_heap[0] * -1

        return max_heap[0] * -1

            

            


