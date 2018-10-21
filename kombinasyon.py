while(True):
    print("(n)")
    print("(r)")

    n=int(input("n= "))
    r=int(input("r= "))
    x=0
    n1=1
    r1=1
    r2=r
    while(x<r2):
        n1=n*n1

        n-=1
        x+=1
    x=0    

    while(x<r2):
        r1=r*r1
        r-=1
        x+=1

    print(int(n1/r1))
    print("\n \n \n")
