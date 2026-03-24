nums=[2,0,2,1,1,0]
start=0
middle=0
end=len(nums)-1

while middle <= end:
    if nums[middle]==0:
        nums[middle],nums[start]=nums[start],nums[middle]
        start+=1
        middle+=1
    elif nums[middle]==2:
        nums[middle],nums[end]=nums[end],nums[middle]
        end-=1
    else:
        middle+=1

print(nums)