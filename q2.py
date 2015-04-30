def check_banana(x):
    a=open(x,"r")
    b=0
    for i in a:
        r=i.lower()
        sub=r.find("banana")
        while sub !=(-1):
            b=b+1
            sub=r.find("banana",(sub+1))
    return(b)

c=check_banana("bannanaa.txt")
print("Number of bananas: ",c)
