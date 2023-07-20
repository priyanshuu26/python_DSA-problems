word="geek for geeks".split()
new=[]
for i in word:
    new.append(((i[0].upper()+ i[1:(len(i)-1)]+i[-1].upper())))
final=(" ".join(new))
print(final)

