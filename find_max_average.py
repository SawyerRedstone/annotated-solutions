# You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
        Keep track of the largest sum in windows size k, then return its average at the end.
        This avoids extra computation by only calculating the average once.
        
        Time: O(n) - Window moves through list of size n.
        Space: O(1) - No additional data structures used.
        """
        # Get sum of first window.
        curr_sum = 0
        for i in range(k):
            curr_sum += nums[i]
        
        # Since we haven't looked at more windows yet, this is currently the max.
        max_sum = curr_sum
        
        # Traverse rest of the list to see if any windows have a larger sum.
        for i in range(k, len(nums)):
            # Keep window size k by removing elem i - k whenever we move forward.
            curr_sum += nums[i] - nums[i - k]
            # Update max sum if applicable.
            max_sum = max(max_sum, curr_sum)
        
        # Return average from window with max sum.
        return max_sum / k
