# Counting Rock Samples 
arr=[345, 604, 321, 433, 704, 470, 808, 718, 517, 811]
sample=[]
range1=int(input("enter the range 1:"))
range2=int(input("enter the range 2:"))
for i in arr:
    if (i>range1) and (i<range2):
        sample.append(i)
print(sample)