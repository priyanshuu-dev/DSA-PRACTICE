class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=[]
        res=[-1] * len(nums)

        for i in range(len(nums)):

            while stack and nums[i] > nums[stack[-1]]:
                a=stack.pop()
                res[a]=nums[i]

            stack.append(i)

        for i in range(len(nums)):

            while stack and nums[i] > nums[stack[-1]]:
                a=stack.pop()
                res[a]=nums[i]


        return res
