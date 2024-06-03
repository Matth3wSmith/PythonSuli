print("1. feladat")
sor=int(input("Sorok száma: "))
oszlop=int(input("Oszlopok száma: "))
karakter=input("Kérek pontosan 1 karaktert: ")
while len(karakter)!=1:
    print("Nem megfelelő méret!")
    karakter=input("Kérek pontosan 1 karaktert: ")

for sor in range(sor):
    print(karakter*oszlop)
