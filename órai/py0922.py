#Irassátok ki az 50 első nemnegatív számot!

for i in range(0,50):
    print(i, end="; ")
else:
    print("\n Kész!")

#Irassátok ki a kétjegyű számokat!

for a in range(10,100):
    print(a, end="; ")
else:
    print("\n Kész!")

#Irassátok ki a 100-nál kisebb 7-tel osztható számokat!

for b in range(7, 101, 7):
    print(b)
else:
    print("\n Kész!")
#Irassátok ki az 500 és 2000 között azokat a számokat ahol a tízesek helyén 0 van
for c in range(501, 2000):
    if (c-1)%100==0 or (c-2)%100==0 or (c-3)%100==0 or (c-4)%100==0 or (c-5)%100==0 or (c-6)%100==0 or (c-7)%100==0 or (c-8)%100==0 or (c-9)%100==0:
       print(c, end=' ');
else:
    print("Kész!")

#Irassátok ki azokat a négyzetszámokat, amelyek 3 számjegyűek
for d in range(1, 50):
    if len(str(d*d))==3:
        print(d);
else:
    print("Kész!!")
    
#Számold meg, mennyi 3 jegyű négyzetszám van
#for d in range(1, 50):
#    if len(str(d*d))==3:
#        negyzetSzam = d*d
#        lista = []
#        lista.append(negyzetSzam)
#        hossz = len(lista)
#        print(negyzetSzam)
#print(hossz)

for d in range(1, 50):
    if len(str(d*d))==3:
        print(d);
        szamok = []
        szamok.append(d)
else:
    print(len(szamok))
