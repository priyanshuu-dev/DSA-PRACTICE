from collections import defaultdict
class Solution(object):
    def findTheDifference(self, s, t):
        freq=defaultdict(int)

        for ch in s:
            freq[ch]+=1
        for ch in t:
            freq[ch]-=1
        for ch in freq:
            if freq[ch]!=0:
                return ch 




        
