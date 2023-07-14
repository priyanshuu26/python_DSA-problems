arr=[3, 7, 2, 5, 8, 9]
index=[[0,5],[3,5],[2,4]]


for i in index:
    a=i[0]
    b=i[1]
    j=0
    for i in range(a,b+1):
        j=arr[i]+j    

    print(f"the sum of range[{a},{b}] is {j}")


