def haromszog():
    oldalak=[]
    for i in range(3):
            szam=input("Kérem a(z) {}. egy egész számot: ".format(i+1))
            while not szam.isnumeric():
                print("Ez nem egész szám!")
                szam=input("Kérem a(z) {}. egy egész számot: ".format(i+1))
            oldalak.append(int(szam))
    return oldalak