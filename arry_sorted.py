# sort an array with ,sort and also without it.

arr=[4,2,5,3]
arr.sort()
print(arr)

j=0
ascending=[]
for i in arr:
    if i<(i+1):
        ascending.append(i)
print(ascending)
