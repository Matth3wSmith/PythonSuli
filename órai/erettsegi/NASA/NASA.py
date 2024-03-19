#Gyártó: Kovács Máté
from NASAclass import *
import math

f=open("NASAlog.txt","r")
adatok=[]
for egySor in f:
    sor=egySor.split("*")
    #Utolsó sor elválasztása a space-nél
    utolso=sor[-1].split(" ")
    sor[-1]=utolso[0]
    sor.append(utolso[1])
    adatok.append(sor)
f.close()

for adat in adatok:
    Keres(adat[0],adat[1],adat[2],adat[3],adat[4])

print("5. feladat: Kérések száma: "+str(len(Keres.keresesek)))
osszMeret=0
for kereses in Keres.keresesek:
    osszMeret+=kereses.ByteMeret

#8. feladat
keresSzam=len(Keres.keresesek)
domainSzam=0

for kereses in Keres.keresesek:
    if kereses.Domain()=="Van":
        domainSzam+=1
arany=domainSzam/keresSzam*100

#9. feladat
allapotok=[0,0,0]
"""for kereses in Keres.keresesek:
    if kereses.allapotKod()=="200":
        allapotok[0]+=1
    elif kereses.allapotKod()=="404":
        allapotok[1]+=1
    elif kereses.allapotKod()=="304":
        allapotok[2]+=1"""

for egyAdat in Keres.keresesek:
    egyAdat.allapotKodok()

kodok=Keres.kodStat.keys()
print("6. feladat: Válaszok összes mérete: {} byte".format(osszMeret))
print("8. feladat: Domain-es kérések: {}%".format(round(arany,2)))
print("9. feladat: Statisztika:")
for kod in kodok:
    print("\t{elso}: {masodik} db".format(elso=kod,masodik=Keres.kodStat[kod]))