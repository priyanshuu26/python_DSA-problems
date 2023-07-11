#Non-Repeating Element

arr= [-1, 2, -1, 3, 2]
j=0
uniq=[]
for i in arr:
    if arr.count(i)<=1:
        print(i)
