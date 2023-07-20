



def calculate(str1):
    vov=0
    let=0
    digit=0
    sp=0
    for i in range(len(str1)):
        if(str1[i]>="a" and str1[i]<="z"):
            if(str1[i]=="a" or str1[i]=="e" or str1[i]=="i" or str1[i]=="o" or str1[i]=="u"):
                vov+=1
            else:
                let+=1
        elif(str1[i]>="0" and str1[i]<="9"):
            digit+=1
        else:
            sp+=1
    print("let",let)
    print("vow",vov)
    print("digit",digit)
    print("sp",sp)
        

calculate("priyanshu@26")


        
