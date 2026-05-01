class Solution(object):
    def maxArea(self, height):
        left=0
        right=len(height)-1
        maximum=0
        while left<right:
            water=(right-left)*min(height[right],height[left])
            maximum=max(maximum,water)

            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maximum