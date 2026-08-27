from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = Counter(nums)

        return [item for item, count in counts.most_common(k)]

        # O(N log K) - Easy but there is a more optimal way than heap
        