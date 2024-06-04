print("1. feladat")
def bekeres():
    print("Adj meg szavakat, amik maximum 12 karakterből állnak. A 'vége' szó begépelésével befejezheted!")
    szoveg=input("Adj meg egy szót: ")
    szavak=[]
    while szoveg!="vége":
        if len(szoveg)>13:
            print("Ez a szó hosszabb mint 12 karakter!")
            szoveg=input("Adj meg egy szót: ")
        else:
            szavak.append(szoveg)
            szoveg=input("Adj meg egy szót: ")


    return szavak

szavak=bekeres()
valogatas=[[],[]]
for szo in szavak:
    if len(szo)%2==0:
        valogatas[0].append(szo)
    else:
        valogatas[1].append(szo)

if len(valogatas[0])>len(valogatas[1]):
    print("\nA páros betűkből álló szavakból van több")
else:
    print("\nA páratlan betűkből álló szavakból van több")

hatBetus=0
szavak.sort()
for szo in szavak:
    if len(szo)==6:
        hatBetus=szo
        break

if hatBetus==0:
    print("\nNincs 6 betűs szó a listában")
else:
    print("\nAz első 6 betűs szó: {}".format(hatBetus))

osszBetuk=0
for szo in szavak:
    osszBetuk+=len(szo)
print("\nÖsszesen {} betűt tároltunk el".format(osszBetuk))