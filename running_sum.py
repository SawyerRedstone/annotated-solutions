# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        """
        Time: O(n) - Traverses nums once to get running sum at each point.
        Space: O(n) if solution list is considered, otherwise O(1).
        """
        # The running sum (AKA prefix sum) always starts with the first number.
        running_sum = [nums[0]]
        
        # Start at index 1 because index 0 was already added.
        for i in range(1, len(nums)):
            # Each new running sum is the previous running sum plus the curr number.
            running_sum.append(running_sum[-1] + nums[i])
        return running_sum
