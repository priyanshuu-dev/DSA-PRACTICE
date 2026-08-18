class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq={}

        for i in range(len(nums2)):
            if nums2[i] in freq:
                freq[nums2[i]]+=1
            else:
                freq[nums2[i]]=1
        ans=[]

        for i in range(len(nums1)):
            if nums1[i] in freq:
                if nums1[i] not in ans:
                    ans.append(nums1[i])
                    
        return ans

                

        