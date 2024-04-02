#Gyártó: Kovács Máté

#1. feladat
f=open("terulet.txt","r",encoding="utf-8-sig")
adatok=[]
for sor in f:
    adatok.append(sor.split())

f.close()

#2. feladat