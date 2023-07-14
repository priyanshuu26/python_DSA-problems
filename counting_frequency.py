# Given an array which may contain duplicates, print all elements and their frequencies.

arr=[10, 20, 20, 10, 10, 20, 5, 20]
unique_elements=set(arr)
for i in unique_elements:
    if i in arr:
       print( i,"count is=",arr.count(i))
        
