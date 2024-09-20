# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Move two pointers towards each other, swapping elements as they go.
        Does not return anything, modifies s in-place instead.
        
        Time: O(N) - Pointers travel through the list.
        Space: O(1) - No additional data structures used.
        """
        # Move two pointers towards each other, swapping elements as they go.
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
