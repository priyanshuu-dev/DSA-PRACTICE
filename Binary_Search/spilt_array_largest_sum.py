class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        smallest=0
        low=max(nums)
        high=sum(nums)

        while low<=high:
            mid=(low+high)//2

            parts=1
            current_sum=0

            for num in nums:
                if current_sum+num <=mid:
                    current_sum+=num
                else:
                    parts+=1
                    current_sum=num

            if parts<=k:
                smallest=mid
                high=mid-1
            else:
                low=mid+1

        return smallest
