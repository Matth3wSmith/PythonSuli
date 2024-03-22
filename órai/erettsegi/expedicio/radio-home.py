from radioClassHome import *


f=open("veetel.txt","r")
adatok=[]
for sor in f:
    adatok.append(sor.strip())

print(adatok)
f.close()

for i in range(0,len(adatok),2):
    egyAdat=adatok[i].split()
    kettoAdat=adatok[i+1]
    Uzenet(egyAdat[0],egyAdat[1],kettoAdat)

#2. feladat
elsoU=Uzenet.uzenetek[0].sorszam
utolsoU=Uzenet.uzenetek[-1].sorszam

#3. feladat
farkasok=[]
for adat in Uzenet.uzenetek:
    if adat.farkas()!=False:
        farkasok.append(adat.farkas())
print(farkasok)

print("2. feladat:")
print("Az első üzenet rögzítője: {}".format(elsoU))
print("Az utolsó üzenet rögzítője: {}".format(utolsoU))

print("3. feladat:")
print("{nap}. nap {}. rádióamatőr".format())

