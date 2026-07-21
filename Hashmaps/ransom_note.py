class Solution(object):
    def canConstruct(self,ransomNote, magazine):
        freq={}
        for i in range(len(magazine)):
            if magazine[i] not in freq:
                freq[magazine[i]]=1
            else:
                freq[magazine[i]]+=1
        count=0
        for i in range(len(ransomNote)):
            if ransomNote[i] in freq:
                count+=1
                freq[ransomNote[i]]-=1

                if freq[ransomNote[i]]==0:
                    del freq[ransomNote[i]]
                

        if count==len(ransomNote):
            return True 
        
        return False
   




     

        

        

        