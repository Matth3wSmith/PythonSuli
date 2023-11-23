import random
#Páros számok kigyűjtése
def parosak(lista):
    parosSzamok=[]
    for i in range(len(lista)):
        if lista[i]%2==0:
            parosSzamok.append(lista[i])
    return parosSzamok

#Páratlan számok kigyűjtése
def paratlanOsszeg(lista):
    paratlanOsszeg = 0
    for i in range(len(lista)):
        if lista[i]%2!=0:
            paratlanOsszeg+=lista[i]
    return paratlanOsszeg

#Hány darab adott számjeggyel kezdődő szám van
def szamjegyekSzama(lista):
    for i in range(0,9):
        szamjegySzam=[]
        for elem in lista:
            szam = str(elem)
            if szam[0]==str(i+1):
                szamjegySzam.append(szam)
        print("Ennyi darab",i+1,"-vel/-val kezdődő számjegy van a listában:",len(szamjegySzam))

#
szamok = []
randomok = 0
for i in range(500):
    randomok = random.randint(10000,99999)
    szamok.append(randomok)

#Páros számok kiíratása
print("Páros számok száma:",len(parosak(szamok)))
#Páratlan számok összeglnek kiíratása
print("Páratlan számok összege:",paratlanOsszeg(szamok))

#Lista kettéválasztása
elsoFele=0
masodikFele=0
for i in range(len(szamok)):
    if i<250:
        elsoFele+=szamok[i]
    else:
        masodikFele+=szamok[i]
if elsoFele > masodikFele:
    print("Az lista első felének összege a nagyobb!")
elif elsoFele < masodikFele:
    print("Az lista második felének összege a nagyobb!")
elif elsoFele == masodikFele:
    print("A lista egyik felének összege és másik felének összege egyenlő")

szamjegyekSzama(szamok)


