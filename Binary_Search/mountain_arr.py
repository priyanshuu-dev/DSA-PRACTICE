class Solution(object):
    def peakIndexInMountainArray(self, arr):
        low=0
        high=len(arr)-1
        peak=0
        
        while low<=high:
            mid=(low+high)//2
            
            

            if arr[mid]<arr[mid+1]:
                low=mid+1
            else:
                peak=mid
                high=mid-1

        return low




