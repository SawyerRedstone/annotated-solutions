# Given an integer array arr, count how many elements x there are, such that x + 1 is also in arr. If there are duplicates in arr, count them separately.

class Solution:
    def countElements(self, arr: List[int]) -> int:
        """
        Complexity where n is len(arr):
        Time: O(n) - Putting nums into a set and looping through arr each take O(n). 
        Space: O(n) - In worst case, each num in arr is unique, so set would contain N elems.
        """
        # Put numbers in a set to easily check existence.
        seen = set(arr)
        # Keep track of how many nums we found that fit the criteria.
        count = 0
        # Loop through the list to check if num + 1 is in arr.
        for num in arr:
            if num + 1 in seen:
                count += 1
        return count
