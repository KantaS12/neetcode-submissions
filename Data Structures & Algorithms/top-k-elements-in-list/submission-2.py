class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    
        # bucket sort

        result = {}
        for num in nums:
            if num not in result:
                result[num] = 1
            else:
                result[num] += 1

        # Now we make a bucket :)
        bucket = [[] for _ in range(len(nums) + 1)] # 0 to nums + 1

        for item, count in result.items():
            bucket[count].append(item) # Highest count is at the end

        res_array = []
        for i in range(len(bucket) -1, -1, -1):

            for num in bucket[i]:
                res_array.append(num)

                if len(res_array) == k:
                    return res_array
