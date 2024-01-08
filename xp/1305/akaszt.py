#Gyártó: Kovács Máté
import random
print("Akasztófa játék")

f=open("szavak.txt","r",encoding="utf-8")
szavak=[]
for elem in f:
    szavak.append(elem.strip())
f.close()

#szó kiválasztása
szo=random.choice(szavak)
#print(szo)

hiba=0
def akasztas(hiba):
    print("hiba:"+str(hiba))
    
    if hiba==1:
        print("_"*11)
    elif hiba==2:
        for _ in range(6):
            print(" "*5+"|")
        print("-"*11)
    elif hiba==3:
        print(" "*5+"_"*6)
        for _ in range(6):
            print(" "*5+"|")
        print("-"*11)
    elif hiba==4:
        print(" "*5+"-"*6)
        for i in range(6):
            if i<2:
                print(" "*5+"|"+" "*4+"|")
            else:
                print(" "*5+"|")
        print("-"*11)
    elif hiba==5:
        print(" "*5+"_"*6)
        for i in range(6):
            if i<2:
                print(" "*5+"|"+" "*4+"|")
            elif i==2:
                print(" "*5+"|"+" "*4+"Q")
            else:
                print(" "*5+"|")
        print("-"*11)
    elif hiba==6:
        print(" "*5+"_"*6)
        for i in range(6):
            if i<2:
                print(" "*5+"|"+" "*4+"|")
            elif i==2:
                print(" "*5+"|"+" "*4+"Q")
            elif i==3:
                print(" "*5+"|"+" "*4+"|")
            else:
                print(" "*5+"|")
        print("-"*11)
    elif hiba==7:
        print(" "*5+"_"*6)
        for i in range(6):
            if i<2:
                print(" "*5+"|"+" "*4+"|")
            elif i==2:
                print(" "*5+"|"+" "*4+"Q")
            elif i==3:
                print(" "*5+"|"+" "*3+"\\|")
            else:
                print(" "*5+"|")
        print("-"*11)
    elif hiba==8:
        print(" "*5+"_"*6)
        for i in range(6):
            if i<2:
                print(" "*5+"|"+" "*4+"|")
            elif i==2:
                print(" "*5+"|"+" "*4+"Q")
            elif i==3:
                print(" "*5+"|"+" "*3+"\\|/")
            else:
                print(" "*5+"|")
        print("-"*11)
    elif hiba==9:
        print(" "*5+"_"*6)
        for i in range(6):
            if i<2:
                print(" "*5+"|"+" "*4+"|")
            elif i==2:
                print(" "*5+"|"+" "*4+"Q")
            elif i==3:
                print(" "*5+"|"+" "*3+"\\|/")
            elif i==4:
                print(" "*5+"|"+" "*3+"/")
            else:
                print(" "*5+"|")
        print("-"*11)
    elif hiba==10:
        print(" "*5+"_"*6)
        for i in range(6):
            if i<2:
                print(" "*5+"|"+" "*4+"|")
            elif i==2:
                print(" "*5+"|"+" "*4+"Q")
            elif i==3:
                print(" "*5+"|"+" "*3+"\\|/")
            elif i==4:
                print(" "*5+"|"+" "*3+"/ \\")
            else:
                print(" "*5+"|")
        print("-"*11)
    return hiba


kitalalt=""
k=0
tippelt=[]
rossztipp=[]
szoHossz=[]
lepes=0
#szó hossza aláhúzásként
for a in range(len(szo)):
    szoHossz.append("_")
    
print("Hibázási lehetőséged: 10")

for b in szoHossz:
    print(b,end=" ")


while kitalalt!=szo:
    if hiba==10:
        print("Fel lettél akasztva! :P")
        break
    print("\nRossz tippeid:"+str(rossztipp))
    tipp=input("Mondj egy tippet!")
    if len(tipp)>1:
        print("Csak egy betűt adj meg!")
    else:
        lepes+=1
        if tipp in szo:
            if tipp in tippelt:
                print("Ez már volt...")
                lepes-=1
            else:
                tippelt.append(tipp)
                print("\nBenne van!")
                for i in range(len(szo)):
                    if tipp==szo[i]:
                        szoHossz[i]=tipp
                for b in szoHossz:
                    print(b,end=" ")
                k+=1
            if k==len(szo):
                print("\nEnnyi tippből sikerült rájönnöd: "+str(lepes))
                print("\nKitaláltad a szót, gratulálok! Legközelebb nem lesz ilyen szerencséd...")
                break
        else:
            if tipp in rossztipp:
                print("Ez már volt...")
                lepes-=1
            else:
                rossztipp.append(tipp)
                hiba+=1
                akasztas(hiba)