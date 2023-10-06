#Mértékegység átváltó
#Kovács Máté 2023. 10. 06
#Projektfeladat

tipusok = ["Hosszúság", "Terület", "Térfogat", "Tömeg", "Űrmérték", "Űrmérték + térfogat"];
egysegek = [["mm", "cm", "dm", "m", "km"],
            ["mm2", "cm2", "dm2", "m2", "km2"],
            ["mm3", "cm3", "dm3", "m3", "km3"],
            ["mg", "cg", "g", "dkg", "kg", "t"],
            ["ml", "cl", "dl", "l", "hl"]]
valtok = [  [10, 10, 10 ,1000, 1],
            [100, 100, 100, 1000000, 1],
            [1000, 1000, 1000, 1000000000, 1],
            [10, 10, 10, 100, 1000, 1],
            [10, 10, 10, 100, 1]]

print("#"*35);
#for elem in tipusok:
#    print(elem)

print("Mértékegységek típusok:")
#Mértékegség típus kiírás
for i,elem in enumerate(tipusok):
    print("\t",str(i+1)+":", elem);

print("\t 0: Kilépés");
print("#"*35);

tipusId="";

#Mértékegység típus bekérés
while tipusId=="" or tipusId not in range(len(tipusok)+1):
    try:
        tipusId = int(input("Válassz!"));
        if  tipusId not in range(len(tipusok)+1):
            raise
    except:
        print("Nem jó! Válassz a listából!")

print("#"*35)
tipusId -=1
print("Mértékegység típus:", tipusok[tipusId])

print("Mértékegységek:")

#Mértékegység  kiírása (Miből)
for i,elem in enumerate(egysegek[tipusId]):
    print("\t",str(i+1)+":", elem);

print("\t 0: Kilépés");
print("#"*35);

egysegId="";

#Mértékegység  bekérése (Miből)
while egysegId=="" or egysegId not in range(len(egysegek[tipusId])+1):
    try:
        egysegId = int(input("Válaszd ki, hogy miből szeretnél átváltani!:"));
        if  egysegId not in range(len(egysegek[tipusId])+1):
            raise
    except:
        print("Nem jó! Válassz a listából!")

print("#"*35)
egysegId-=1
print("Kívánt mértékegységből való átváltás:", egysegek[tipusId][egysegId])


#Mértékegység kiírása (Mibe)
for i,elem in enumerate(egysegek[tipusId]):
    print("\t",str(i+1)+":", elem);

print("\t 0: Kilépés");
print("#"*35);

egysegId2="";

#Mértékegység bekérése (Mibe)
while egysegId2=="" or egysegId not in range(len(egysegek[tipusId])+1):
    try:
        egysegId2 = int(input("Válaszd ki, hogy mibe szeretnél átváltani!:"));
        if  egysegId2 not in range(len(egysegek[tipusId])+1):
            raise
    except:
        print("Nem jó! Válassz a listából!")


egysegId2-=1
print("#"*35)
print("Kívánt mértékegységbe váltás:", egysegek[tipusId][egysegId2])

szam=float(input("Írd be az átváltani kívánt mennyiséget!:"))

if egysegId<egysegId2:
    #print(valtok[tipusId][egysegId:egysegId2])
    szorzo = 1
    for e in valtok[tipusId][egysegId:egysegId2]:
        szorzo *= e
    eredmeny = szam/szorzo
else:
    #print(valtok[tipusId][egysegId2:egysegId])
    szorzo = 1
    for e in valtok[tipusId][egysegId2:egysegId]:
        szorzo *= e
     eredmeny = szam*szorzo

print(szam, egysegek[tipusId][egysegId], eredmeny, egysegek[tipusId][egysegId2])


#Házi: Csinosítás, számbekérésnél ellenőrzés hogy szám-e, while try, addig kell csinálni amig a tipusválasztónál a kilépést nem választjuk, (egészet egy while-ba)
