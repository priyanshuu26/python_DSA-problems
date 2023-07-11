# Given two arrays: a1[0..n-1] of size n and a2[0..m-1] of size m. Task is to check whether a2[] is a subset of a1[] or not. Both the arrays can be sorted or unsorted. There can be duplicate elements.

a1= [1, 2, 3, 4, 4, 5, 6]
a2= [1, 2,9]
output=[]
for i in  a2:
    if i in a1:
        output.append(i)
if len(output)==len(a2):
    print("yes")
else:
    print("no")