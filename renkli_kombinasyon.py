import os
normal = '\033[0m'
kirmizi= '\033[31m'
yesil= '\033[32m'
sari= '\033[33m'
lacivert= '\033[34m'
mor= '\033[35m'
mavi= '\033[36m'
pmavi = '\033[96m'#p --> parlak
pkirmizi= '\033[91m'
pyesil = '\033[92m'
psari = '\033[93m'
siyah = '\033[90m'
asiyah= '\033[40m'#a --> arkaplan
akirmizi= '\033[41m'
ayesil= '\033[42m'
asari= '\033[43m'
alacivert= '\033[44m'
amor= '\033[45m'
amavi= '\033[46m'
abeyaz= '\033[47m'
apsiyah= '\033[100m'#a --> arkaplan-parlak
apkirmizi= '\033[101m'
apyesil= '\033[102m'
apsari= '\033[103m'
aplacivert= '\033[104m'
apmor= '\033[105m'
apmavi= '\033[106m'
apbeyaz= '\033[107m'
while(True):

    print(pyesil+"C(n,r)")
   

    n=int(input(pmavi+"n= "+mor))
    r=int(input(pmavi+"r= "+mor))
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
    print("\n ")
    os.system("clear")
    print(psari+str(int(n1/r1)))
    print("")
   
