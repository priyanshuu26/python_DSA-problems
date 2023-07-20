arr1=[[1,2],[3,4]]
arr2=[[4,3],[2,1]]

for i in range(len(arr1)):
    print(arr1[i][i]+arr2[i][i])
    print(arr1[i][i-1]+arr2[i][i-1])
