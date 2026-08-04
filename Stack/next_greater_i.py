class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        stack=[]
        res=[-1]*len(nums2)

        for i in range(len(nums2)):

                while stack and nums2[i]>nums2[stack[-1]]:
                    a=stack.pop()
                    res[a]=nums2[i]


                stack.append(i)

        freq ={}
        for i in range(len(nums2)):
            freq[nums2[i]]=i
            
        ans=[]
        for i in range(len(nums1)):
            
            x=freq[nums1[i]]
            ans.append(res[x])
            
        return ans