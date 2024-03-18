#Gyártó: Kovács Máté
from NASAclass import *

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
print("6. feladat: Válaszok összes mérete: "+str(osszMeret))
