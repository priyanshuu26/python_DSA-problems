word="GeeksForgEeks"
new=[]
for i in word:
    if(i>="A" and i<="Z"):
        i=i.lower()
        new.append(i)
    elif(i>="a" and i<="z"):
        i=i.upper()
        new.append(i)
print("".join(new))