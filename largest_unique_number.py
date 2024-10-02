# Given an integer array nums, return the largest integer that only occurs once. If no integer occurs once, return -1.

from collections import Counter

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        """
        Time: O(nlogn) - Sorting the numbers is the bottleneck and takes O(nlogn).
        Space: O(n) - Dict containing freq of n numbers.
        """
        freq = Counter(nums)
        
        # Sort keys in reverse so the first solution found will be the largest.
        for num in sorted(freq.keys(), reverse=True):
            if freq[num] == 1:
                return num
            
        # If it didn't return anything yet, there were no unique numbers.
        return -1
            
        
