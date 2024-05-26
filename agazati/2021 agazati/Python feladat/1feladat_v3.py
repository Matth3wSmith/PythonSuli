print("1. feladat")
szoveg=input("Kérek egy szöveget! ")
szam=input("Kérek egy egész számot! ")

if szam.isnumeric():
    szam=int(szam)
    print(szoveg[szam]*szam)
else:
    print("Ez nem egész szám!")
    szam=input("Kérek egy egész számot! ")