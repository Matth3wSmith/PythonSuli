#Gyártó: Kovács Máté
from NASAclass import *

f=open("NASAlog.txt","r")
adatok=[]
for egySor in f:
    sor=egySor.split("*")
    utolso=sor[-1].split(" ")
    sor[-1]=utolso[0]
    sor.append(utolso[1])
    adatok.append(sor)
f.close()

print(adatok[-1])
for adat in adatok:
    Keres(adat[0],adat[1],adat[2],adat[3],adat[4])

print(len(Keres.keresesek))