class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # target = num1 + num2

        # O(N^2) approach is to go over the array 2 times 
        # to find index 1 and index 2

        # How about we do a num2 = target - num1 ?
        # Attach the indexes per nums
        # Hash table it (dict)

        # Put into dictionary
        nums_dict = {}

        # key: number, val: index

        # Let's go through the array
        for i in range(len(nums)):

            nums1 = nums[i]
            nums2 = target - nums1

            if nums2 in nums_dict:
                return [nums_dict[nums2], i]

            nums_dict[nums1] = i


