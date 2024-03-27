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

#3. feladat
print("\n3. feladat:")
for uzenet in uzenetek:
    if uzenet.farkasKereso():
        print("{nap}. nap {sorszam}. rádióamatőr".format(nap=uzenet.nap, sorszam=uzenet.amator))

#4. feladat
napok=[]
tempNap=Nap(1)
for uzenet in uzenetek:
    pass
