# Let us consider the following problem to understand MO’s Algorithm.
# We are given an array and a set of query ranges, we are required to find the sum of every query range:
arr=[1, 1, 2, 1, 3, 4, 5, 2, 8]
index=[[0, 4], [1, 3], [2, 4]]

for i in index:
    a=(i[0])
    b=(i[1])
    # print(a,b)
    j=0
    for i in range(a,b+1):
        j=arr[i]+j
    # print(j)
    print(f"the sum of range[{a},{b}] is {j}")
