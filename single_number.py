class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        """
        LeetCode 136 - Single Number

        Approach:
        Use XOR to cancel out duplicate elements.
        - a ^ a = 0
        - a ^ 0 = a
        So, all duplicate numbers cancel out, leaving the unique number.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        result = 0

        for num in nums:
            result ^= num

        return result