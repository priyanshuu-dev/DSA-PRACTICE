class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        freq1={}
        freq2={}

        for i in range(len(s)):
            if s[i] not in freq1:
                freq1[s[i]]=1
            else:
                freq1[s[i]]+=1
        for j in range(len(t)):
            if t[j] not in freq2:
                freq2[t[j]]=1
            else:
                freq2[t[j]]+=1
        if freq1==freq2:
            return True
        return False