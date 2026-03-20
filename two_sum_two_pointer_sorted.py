arr=[2,7,5,11,3]
target=9
arr.sort()
l=0
r=len(arr)-1
while l<r:
    sum=arr[l]+arr[r]
    if sum==target:
        print(arr[l],arr[r])
        break
    elif sum>target:
        r-=1
    else:
        l+=1





    
