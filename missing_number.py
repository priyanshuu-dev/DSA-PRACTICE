class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        """
        LeetCode 268 - Missing Number
        
        Approach:
        Use the sum formula to calculate the expected sum of numbers from 0 to n.
        Then subtract the actual sum of the array to find the missing number.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        
        n = len(nums)
        
        # Expected sum of numbers from 0 to n
        expected_sum = n * (n + 1) // 2
        
        # Actual sum of elements in the array
        actual_sum = sum(nums)
        
        # Missing number is the difference
        return expected_sum - actual_sum