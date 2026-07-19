class Solution(object):
    def maxSubArray(self, nums):
        best_ending=nums[0]
        ans=nums[0]
        for i in range(1,len(nums)):
            sum1=best_ending +nums[i]
            sum2=nums[i]

            best_ending=max(sum1,sum2)
            ans=max(ans,best_ending)

        return ans