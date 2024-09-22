# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        Time: O(n) - Window moves through list of size n.
        Space: O(1) - No additional data structures used.
        """
        # Make sure window never contains more than k 0s.
        zero_count = 0
        longest_chain = 0
        left = 0
        for right in range(len(nums)):
            if nums[right]  == 0:
                zero_count += 1
            # If window contains too many 0s, move left ptr until window is fixed.
            while zero_count > k:
                # Remove value at left pointer before shifting it over.
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            # Update longest_chain if the curr window size is the new max.
            longest_chain = max(longest_chain, right - left + 1)
        return longest_chain
        
        
