from furdoClass import *

def idoVissza(mp):
    ora=mp//(60*60)
    perc=mp%3600//60
    sec=mp%3600%60
    return str(ora)+":"+str(perc)+":"+str(sec)

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

#4. feladat

kezdes=0
idoMax=0
vendeg=0
for egyElem in vendegek:
    if egyElem.belepett and egyElem.reszleg==0:
        bentiIdo=egyElem.idoSec()-kezdes
        if bentiIdo>idoMax:
            idoMax=bentiIdo
            vendeg=egyElem.vendeg
    if not egyElem.belepett and egyElem.reszleg==0:
        kezdes=egyElem.idoSec()

print("\n4. feladat")
print("A legtöbb időt eltöltő vendég: ")
print("{}. vendeg {}".format(vendeg,idoVissza(idoMax)))

#5. feladat
stat=[0,0,0]

for egyElem in vendegek:
    if egyElem.reszleg==0 and not egyElem.belepett:
        if egyElem.ora<9:
            stat[0]+=1
        elif egyElem.ora<16:
            stat[1]+=1
        else:
            stat[2]+=1

print("\n5. feladat:")
print("6-9 óra között {} vendég".format(stat[0]))
print("9-16 óra között {} vendég".format(stat[1]))
print("16-20 óra között {} vendég".format(stat[2]))

#6. feladat
szaunastat={}
for egyElem in vendegek:
    if egyElem.vendeg not in szaunastat.keys():
        szaunastat[egyElem.vendeg]=0
    if egyElem.reszleg==2:
        if egyElem.belepett:
            kezdoBentiIdo=egyElem.idoSec()
        if not egyElem.belepett:
            bentiIdo=egyElem.idoSec()-kezdoBentiIdo
            szaunastat[egyElem.vendeg]+=bentiIdo
print(szaunastat)
f=open("szauna.txt","w")
for kulcs in szaunastat.keys():
    if szaunastat[kulcs]!=0:
        f.write("{} {}\n".format(kulcs,idoVissza(szaunastat[kulcs])))
f.close()
    
#7. feladat
reszlegStat={}
for egyElem in vendegek:
    if egyElem.reszleg not in reszlegStat.keys():
        reszlegStat[egyElem.reszleg]=0
                