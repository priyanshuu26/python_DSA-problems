arr=[23,55,65,74,78,3]
def isSort(array):
    arr.sort()

    new=[]
    j=array[0]
    for i in range(len(array)):
        if(j>arr[i]):
            j=array[i]
        new.append(array[i])
    return new

for i in range(len(arr)):
    if(arr[i]==isSort(arr[i])):
        print("yes")
    else:
        print("no")