arr=[7, 2, 3, 0, 5, 10, 3, 12, 18]
index= [[0, 4], [4, 7], [7, 8]]

for i in index:
    a=i[0]
    b=i[1]
    for j in range(a,b+1):
        if(arr[a]>arr[j]):
            arr[a]=arr[j]
    print(f"Minimum of [{a}, {b}] is  {arr[a]}")
       