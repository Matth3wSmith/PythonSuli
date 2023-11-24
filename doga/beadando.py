import random
#1 Hány páros szám van a listában
def parosSzamok(listanev):
    parosSzamok=[]
    for elem in listanev:
        if elem%2==0:
            parosSzamok.append(elem)
    print("Ennyi páros szám van a listában",len(parosSzamok))
    print("#"*30)

#2 Mennyi a páratlan számok összege 
def paratlanOsszeg(listanev):
    paratlanOsszeg = 0
    for elem in listanev:
        if elem%2!=0:
            paratlanOsszeg+=elem
    print("Ennyi a páratlan számok összege:",paratlanOsszeg)
    print("#"*30)

#3 Első fél--második fél
def melyikNagyobb(listanev):
    elsoFel=0
    masodikFel=0
    for i in range(len(listanev)):
        if i<250:
            elsoFel+=listanev[i]
        else:
            masodikFel+=listanev[i]
    if elsoFel>masodikFel:
        print("A lista első felének összege a nagyobb!")
        print("#"*30)
    elif elsoFel<masodikFel:
        print("A lista második felének összege a nagyobb!")
        print("#"*30)
    elif elsoFel==masodikFel:
        print("A lista első felének összege egyenlő a lista második felének összegével!")
        print("#"*30)

#6 Mennyi adott számjeggyel kezdődő szám van
def szamjegy(listanev):
    for i in range(9):
        szamjegySzam=0
        for k in range(len(listanev)):
            szam=str(listanev[k])
            if szam[0] == str(i+1):
                szamjegySzam=szamjegySzam+1
        print(i+1,"-val/vel kezdődő szám van:",szamjegySzam)
    print("#"*30)

#1 Számok generálása
szamok=[]

for i in range(0,500):
    szamok.append(random.randint(10000,99999))

#2
parosSzamok(szamok)
#3
paratlanOsszeg(szamok)
#4
melyikNagyobb(szamok)

#5 Mennyi 3-mal kezdődő szám van
szamjegySzam=0
for k in range(len(szamok)):
    szam=str(szamok[k])
    if szam[0] == str(3):
        szamjegySzam=szamjegySzam+1
print("Ennyi 3-mal kezdődő szám van:",szamjegySzam)
print("#"*30)

#6
szamjegy(szamok)
