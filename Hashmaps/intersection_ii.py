class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq={}
        for i in range(len(nums2)):
            if nums2[i] in freq:
                freq[nums2[i]]+=1
            else:
                freq[nums2[i]]=1
        ans=[]

        for i in range(len(nums1)):
            if nums1[i] in freq:
                ans.append(nums1[i])

                freq[nums1[i]]-=1

                if freq[nums1[i]]==0:
                    del freq[nums1[i]]

        return ans