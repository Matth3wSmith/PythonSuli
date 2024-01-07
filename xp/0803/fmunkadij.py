#Gyártó: Kovács Máté
import math

f=open("munkak.txt","a",encoding="utf-8")
dolgozokSzama=int(input("Add meg, hogy hány dolgozó adatait szeretnéd megadni:"))
for i in range(dolgozokSzama):
    azonosito=str(input("Add meg az azonosoítódat:"))
    oraber=int(input("Add meg az órabéred:"))
    orak=int(input("Add meg a heti ledolgozott óráid számát:"))

    munkaber=40*oraber+(orak-40)*(1.5*oraber) if orak>40 else oraber*orak

    f.write(azonosito+":"+str(oraber)+":"+str(orak)+":"+str(munkaber)+"\n")

    print("A munkabéred: "+str(munkaber))