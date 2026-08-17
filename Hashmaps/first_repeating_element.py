class Solution:
    def firstRepeated(self, arr):
        # code here 
        freq={}
        for i in range(len(arr)):
            if arr[i] in freq:
                freq[arr[i]]+=1
            else:
                freq[arr[i]]=1
        res=0       
        for num,count in freq.items():
            if count>1:
                res=num
                break
        for i in range(len(arr)):
            if arr[i]==res:
                return i+1
                
        return -1