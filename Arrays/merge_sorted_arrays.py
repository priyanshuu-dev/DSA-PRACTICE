arr1=[1,3,5]
arr2=[2,4,6]
arr3=[]
pt1=0
pt2=0
while pt1<len(arr1) and pt2<len(arr2):
    if arr1[pt1]<arr2[pt2]:
        arr3.append(arr1[pt1])
        pt1+=1
    else:
        arr3.append(arr2[pt2])
        pt2+=1
while pt1<len(arr1):
        arr3.append(arr1[pt1])
        pt1+=1

while pt2<len(arr2):
    arr3.append(arr2[pt2])
    pt2+=1

print(arr3)

