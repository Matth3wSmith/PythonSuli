from modul import *

print("2. feladat")
korok=[]
for i in range(5):
    korok.append(kor())

for korI in range(1,len(korok)):
    if viszony(korok[0],korok[korI])=="Metsz":
        print("Van, amelyik metszi az elsőt.")