class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # sort array first (easier)
        nums.sort()

        result = []

        # Define Pointers
        for i in range(len(nums)):

            left = i + 1
            right = len(nums) - 1

            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            while left < right:

                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    left += 1

                    while left < right and nums[left] == nums[left- 1]:
                        left += 1

                elif current_sum < 0:
                    left += 1

                else:
                    right -=1
        return result




        