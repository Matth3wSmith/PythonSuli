from furdoClass import *

#1. feladat
f=open("furdoadat.txt","r")
vendegek=[]
for sor in f:
    vendegek.append(Furdo(sor))

f.close()

#2. feladat
print("2.feladat")
print("Az első vendég {}-kor lépett ki az öltözőből".format(vendegek[0].ido()))
utolso=vendegek[0]
for egyElem in vendegek:
    if not egyElem.belepett and egyElem.reszleg==0:
        utolso=egyElem
print("Az utolsó vendég {}-kor lépett ki az ötlözőből".format(utolso.ido()))

#3. feladat
darab=0
elozo=-1
temp=1
for egyElem in vendegek:
    if elozo==egyElem.vendeg:
        temp+=1
    else:
        if temp==4:
            darab+=1
        elozo=egyElem.vendeg
        temp=1
print("\n3. feladat")
print("A fürdőben {} vendég fárt csak egy részlegen.".format(darab))