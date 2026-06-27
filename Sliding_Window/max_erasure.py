class Solution(object):
    def maximumUniqueSubarray(self, nums):
        low=0
        maximum=0
        seen=set()
        current_sum=0
        for high in range(len(nums)):
            while nums[high] in seen:
                seen.remove(nums[low])
                current_sum-=nums[low]
                low+=1

            seen.add(nums[high])
            current_sum+=nums[high]

            maximum=max(maximum,current_sum)


        return maximum