class Solution(object):
    def maxNumberOfBalloons(self, s):

        b="balloon"
        if len(s)<len(b):
            return 0
        freq={}

        for i in range(len(s)):
            if s[i] not in freq:
                freq[s[i]]=1
            else:
                freq[s[i]]+=1

        b=freq.get("b",0)
        a=freq.get("a",0)
        l=freq.get("l",0)//2
        o=freq.get("o",0)//2
        n=freq.get("n",0)

        return min(b,a,l,o,n)

        
                


       

        
        
        

           





     
        