class Solution(object):
    def majorityElement(self, nums):
        freq={}
        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]]=1
            else:
                freq[nums[i]]+=1
        max=float("-inf")
        ans=-1
        for key,value in freq.items():
            if value>max:
                max=value
                ans=key
        return ans
            


        

            
        
            

        
        