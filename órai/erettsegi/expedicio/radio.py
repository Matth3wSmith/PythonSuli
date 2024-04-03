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
nap=1
while nap!=12:
    tempNap=Nap(nap)
    for uzenet in uzenetek:
        if uzenet.nap==nap:
            tempNap.hozzaAd(uzenet)
    napok.append(tempNap)
    nap+=1

print("\n4. feladat:")
for nap in napok:
    print("{nap}. nap: {amator} rádióamatőr".format(nap=nap.nap,amator=nap.uzenetSzam()))
print(len(napok))

#Házi feladat: OPP program szorzótábla sorait tartalmazza, ennek segítségével 10x10-es szorzótábla készítése. Egy class egy sor adatai