#to find the mean and mode of the given array:

arr=[1, 3, 4, 2, 6, 5, 8,7]
arr.sort()


#mean:
j=0
for i in arr:
    j=i+j
mean=j/(len(arr))
print("mean",mean)

#median:
if (len(arr)%2==0):
    elememt2=int(len(arr)/2)
    elememt1=elememt2-1
    median=(arr[elememt2]+arr[elememt1])/2
    print("median",median)
else:
    median=round(int(len(arr)/2))
    med=median-1
    print("median",arr[med-1])