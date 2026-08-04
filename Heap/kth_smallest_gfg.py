import heapq
class Solution:
    def kthSmallest(self, nums, k):
        # Code here
        heap=[]
        
        for i in range(len(nums)):
            heapq.heappush(nums[i],heap)
            
        while k:
            a=heapq.heappop(heap)
            k-=1
            
        return a