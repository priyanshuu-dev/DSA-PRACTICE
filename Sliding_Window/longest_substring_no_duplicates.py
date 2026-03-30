class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        low = 0
        maximum = 0
        val = []
        
        for high in range(len(s)):
            # 1. Expand the window by adding the current character
            val.append(s[high])

            # 2. If there's a duplicate, shrink from the left
            while len(set(val)) != len(val):
                val.pop(0)
                low += 1

            # 3. Once valid, calculate the length and update maximum
            length = high - low + 1
            if length > maximum:
                maximum = length
                
        return maximum

# Example usage:
# sol = Solution()
# print(sol.lengthOfLongestSubstring("abcabcbb"))

        
