class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        low = 0
        high = 0
        maximum = 0
        val = {}
        
        while high < len(s):
            if s[high] not in val:
                val[s[high]] = high
                length = high - low + 1
                if length > maximum:
                    maximum = length
                high += 1
            else:
                if s[low] in val:
                    del val[s[low]]
                low += 1
                
        return maximum


        
        