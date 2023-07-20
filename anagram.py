a = "army".replace(""," ").split()
b = "marm".replace(""," ").split()
a.sort()
b.sort()
for i in range(0,len(a)):
    if(a[i]== b[i]):
        print("anagram")    
    else:
        print("not an anagram")