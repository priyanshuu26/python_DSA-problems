n=13
for i in range(2,int(n/2)+1):
    if(n%i==0):
        print("not prime")
        break
else:
    print("prime")
        