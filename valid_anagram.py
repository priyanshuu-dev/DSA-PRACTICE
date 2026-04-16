from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        """
        Check if two strings are anagrams.

        An anagram is formed by rearranging the letters
        of a word to produce another word using all original letters.

        :type s: str
        :type t: str
        :rtype: bool
        """
        
        # If lengths differ, they cannot be anagrams
        if len(s) != len(t):
            return False

        # Compare frequency of characters
        return Counter(s) == Counter(t)