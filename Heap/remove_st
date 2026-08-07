import heapq
class Solution:
    def minStoneSum(self, nums: List[int], k: int) -> int:
        heap=[]
        for i in range(len(nums)):
            heapq.heappush(heap,-nums[i])

        while k:
            pile=heapq.heappop(heap)
            pile=pile*(-1)
            remove=pile//2
            pile=pile-remove

            if pile>0:
                heapq.heappush(heap,-pile)

            k-=1

        ans=0
        while heap:
            ans+=-heapq.heappop(heap)

        return ans

