class Solution(object):
    def findMaxAverage(self, nums, k):
        low=0
        total=0
        avg=0
        maximum=float('-inf')
        for high in range(len(nums)):
            total+=nums[high]
            avg=total/float(k)

            if high-low+1==k:

                if avg>maximum:
                    maximum=avg

                total-=nums[low]
                low+=1
        return maximum