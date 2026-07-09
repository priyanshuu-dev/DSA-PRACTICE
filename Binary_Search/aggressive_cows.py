class Solution:
    def aggressiveCows(self, arr, k):
        arr.sort()
        low=1
        high=arr[-1]-arr[0]
        smallest=0
        
        while low<=high:
            mid=(low+high)//2
            
            count=1
            last=arr[0]
            
            for i in range(1,len(arr)):
                if arr[i]-last>=mid:
                    count+=1
                    last=arr[i]
                
            if count>=k:
                smallest=mid
                low=mid+1
            else:
                high=mid-1
        return smallest