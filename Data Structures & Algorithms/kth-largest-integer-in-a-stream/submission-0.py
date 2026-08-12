import heapq

class KthLargest:

    # left = 2i + 1
    # right = 2i + 2

    # parent = (i -1) // 2
    def __init__(self, k: int, nums: List[int]):
        self.lists = nums
        self.k = k
        heapq.heapify(self.lists) #Creates a minheap using list nums

    def add(self, val: int) -> int:
        heaps = heapq.heappush(self.lists, val)
        while len(self.lists) > self.k:
            heapq.heappop(self.lists)

        return self.lists[0]
