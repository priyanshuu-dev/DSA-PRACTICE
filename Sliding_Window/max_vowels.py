class Solution(object):
    def maxVowels(self, s, k):
        vowels = "aeiou"
        count = 0
        maximum = 0
        low = 0

        for high in range(len(s)):
            
            # add new character
            if s[high] in vowels:
                count += 1
            
            # maintain window size k
            if high - low + 1 > k:
                if s[low] in vowels:
                    count -= 1
                low += 1
            
            # update answer when window size is exactly k
            if high - low + 1 == k:
                maximum = max(maximum, count)
        
        return maximum