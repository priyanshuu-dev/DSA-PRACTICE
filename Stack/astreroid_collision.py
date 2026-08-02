# leetcode 735
class Solution:
    def asteroidCollision(self, nums: List[int]) -> List[int]:
        stack=[]

        for i in range(len(nums)):
            coming=True


            while stack and stack[-1]>0 and nums[i]<0:
                if -nums[i] > stack[-1]:
                    stack.pop()
                    
                elif -nums[i]<stack[-1]:
                    coming=False
                    break

                else:
                    stack.pop()
                    coming=False
                    break

            if coming:
                stack.append(nums[i])

        return stack