class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    
        # My idea is we're given a m x n array so what we could do is we do binary search from the first index of each array (O(1)). So if middle array first index is less than target then we look into the middle array + right side (which is more ). 
        # Then we do another binary search where we find the middle of the inside of the array and if the target is less than middle then we look into left, else it's right. 
        # It should. be o(log n * m) since we're doing binary 2 times. 

        def search_2d(matrix, target):
            td_left = 0
            td_right = len(matrix) - 1
            td_start = 0

            while td_left <= td_right:

                td_middle = (td_left + td_right) // 2

                # We look at the middle array first index
                td_start = matrix[td_middle][0]
                td_end = matrix[td_middle][-1]

                if target < td_start:
                    td_right = td_middle - 1

                elif target > td_end:
                    td_left = td_middle + 1

                else:
                    return td_middle

            return -1

        correct_index = search_2d(matrix, target)

        if correct_index == -1:
            return False
        
        left = 0
        right = len(matrix[correct_index]) - 1

        while left <= right:

            mid = (left + right) // 2

            if target == matrix[correct_index][mid]:
                return True

            elif target > matrix[correct_index][mid]:
                left = mid + 1

            else:
                right = mid - 1

        return False




