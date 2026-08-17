class Solution:
    def frequencyCount(self, arr):
        #  code here
        freq={}
        for i in range(len(arr)):
            if arr[i] in freq:
                freq[arr[i]]+=1
            else:
                freq[arr[i]]=1
                
        n=len(arr)
        res=[0]*n
        
        for num,count in freq.items():
            res[num-1]=count
  
        return res
