# Given an unsorted array arr[] , Rotate the array to the left (counter-clockwise direction) by D steps, where D is a positive integer. 

arr=[1,2,3,4,5]
n=2
length=len(arr)
first=(arr[:n])
second=(arr[n:])
print(second+first)