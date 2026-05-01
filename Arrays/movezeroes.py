class Solution(object):
    def moveZeroes(self, nums):
        
        low=0
        for high in range(len(nums)):
            if nums[high]!=0:
                nums[high],nums[low]=nums[low],nums[high]
                low+=1
                
