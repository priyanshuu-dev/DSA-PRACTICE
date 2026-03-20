arr=[-4,-1,0,3,10]
arr1=[]
arr2=[]

first=0
second=0
sortedd=[]


for i in range(len(arr)):
    if arr[i]<0:
        arr1.append(arr[i] ** 2)
        
    else:
        arr2.append(arr[i] **2)


arr1=arr1[::-1]


while first<len(arr1) and second<len(arr2):
    if arr1[first]<arr2[second]:
       sortedd.append(arr1[first])
       first+=1
       
    else:
        sortedd.append(arr2[second])
        second+=1


while first < len(arr1):
    sortedd.append(arr1[first])
    first += 1

    
while second < len(arr2):
    sortedd.append(arr2[second])
    second += 1

print(sortedd)

