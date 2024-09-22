# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

# Solution 1, using math.
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """ 
        Find total sum if no numbers were missing. 
        Then subtract that by the sum of nums to see which number we're missing.

        Time: O(n) - Summing nums of length n.
        Space: O(1) - No additional data structures used.
        """
        largest_num = len(nums)
        range_size = len(nums) + 1

        # Find middle value in the range.
        mid = largest_num / 2
        # Treat each number in range as this middle value to get total sum.
        total_sum = mid * range_size
        # Find missing number by subtracting sum of numbers we have. 
        return int(total_sum - sum(nums))


# Solution 2, using a set.
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Time: O(n) - Creating set size n and looping through range of n + 1.
        Space: O(n) - The set contains n numbers.
        """
        # Number order doesn't matter, so use a set for quicker lookups.
        num_set = set(nums)
        # Loop through range to check which number is missing from the set.
        for num in range(len(num_set) + 1):
            if num not in num_set:
                return num
