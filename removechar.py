word="computer".replace(""," ").split()
j=[]
remove="cat".replace(""," ").split()
for i in word:
    if i not in remove:
        j.append(i)
new=(" ".join(j)).replace(" ","")
print(new)

