#print the smallest and second smallest number fro the array:


arr=[12, 13,2, -10, 34]
j=arr[0]
for i in arr:
    if(j>=i):
        j=i
print("smallest",j)
arr.remove(j)

arr2=arr
m=arr2[0]
for k in arr2:
    if(m>=k):
        m=k
print("second smallest:",m)