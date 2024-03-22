from radioClass import *

f=open("veetel.txt","r")

sorszam=0
tempSor=""
uzenetek=[]

for egySor in f:
    if sorszam%2==0:
        tempSor=egySor
    else:
        uzenetek.append(Uzenet(tempSor,egySor))
    sorszam+=1

print(uzenetek)
f.close()

print("2. feladat:")
print("Az első üzenet rögzítője: {}".format(uzenetek[0].amator))
print("Az utolsó üzenet rögzítője: {}".format(uzenetek[-1].amator))

