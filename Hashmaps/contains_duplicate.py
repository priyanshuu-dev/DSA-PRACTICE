class Solution(object):
    def containsDuplicate(self, nums):
        freq={}

        for i in range(len(nums)):
            if nums[i] in freq:
                return True
            freq[nums[i]]=1

        return False
         
        

        