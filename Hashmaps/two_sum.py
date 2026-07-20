class Solution(object):
    def twoSum(self, nums, target):
        freq={}

        for i in range(len(nums)):
            rem=target-nums[i]

            if rem in freq:
                return [freq[rem],i]

            freq[nums[i]]=i