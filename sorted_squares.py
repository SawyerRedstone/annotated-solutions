# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """ 
        After squaring, the left and rightmost sides will be largest.
        Using two pointers, we can keep adding the larger one to the the solution list.

        Time: O(N) - Together, the left and right pointers traverse the entire list of size n. 
        Space: O(N) if the output list is considered, O(1) otherwise.
        """
        # Make an empty list to fill with sorted values.
        result = [None] * len(nums)
        # Use pointers on left and right side to compare largest values.
        left = 0
        right = len(nums) - 1
        # Keep adding largest squared values to the result list.
        # Squares will keep getting smaller as we near the center, so we'll start adding at the end.
        result_ptr = len(result) - 1 
        while left <= right:
            squared_left = nums[left] ** 2
            squared_right = nums[right] ** 2
            if squared_left > squared_right:
                result[result_ptr] = squared_left
                left += 1
            else:
                result[result_ptr] = squared_right
                right -= 1
            result_ptr -= 1
        return result
