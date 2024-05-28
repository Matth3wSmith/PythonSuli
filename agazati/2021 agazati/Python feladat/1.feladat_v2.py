szoveg=input("Kérek egy szöveget: ")
while True:
    try:
        szam=int(input("Kérek egy egész számot: "))
    except:
        print("Ez nem egész szám!")
    else:
        break

try:
    print(szoveg[szam-1]*szam)
except:
    print("Sajnos nincs ilyen betű.")