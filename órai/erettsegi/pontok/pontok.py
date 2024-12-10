#Informatika érettségi 2015. október 12.
#
#
#1. feladat
f=open("pontok.txt","r")
pontok={}
for sor in f:
    key,values= sor.split("=")
    key=int(key.split("(")[1][0:3])
    values=list(map(int,values.split(",")))
    pontok[key]={"x":values[0],"y":values[1]}
f.close()
print(f"1. feladat: Pontok száma a pontok.txt állományban: {len(pontok)} db")

#2. feladat
tengelyen=0
for value in pontok.values():
    if (value["x"]==0 or value["y"]==0):
        tengelyen+=1

print(f"2. feladat: Pontok száma az x vagy y tengelyen: {tengelyen} db")

#3. feladat
azonosKulcs=[]

