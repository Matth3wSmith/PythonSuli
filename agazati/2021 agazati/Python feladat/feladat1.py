szoveg=input("Kérek egy szöveget: ")
szam=input("Kérek egy egész számot: ")
while not szam.isnumeric():
    print("Ez nem egész szám!")
    szam=input("Kérek egy egész számot: ")
szam=int(szam)
print(szoveg[szam]*szam)