import re
word=("what is your name ?").replace(" ","")

for i in range(0,len(word)):
    ch=word[i]
    if(ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u"):
        print(word.sub(ch))

        
        