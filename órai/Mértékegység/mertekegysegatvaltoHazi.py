#Mértékegység átváltó
#Kovács Máté 2023. 10. 06
#Projektfeladat

tipusok = ["Hosszúság", "Terület", "Térfogat", "Tömeg", "Űrmérték", "Űrmérték + térfogat"];
egysegek = [["mm", "cm", "dm", "m", "km"],
            ["mm2", "cm2", "dm2", "m2", "km2"],
            ["mm3", "cm3", "dm3", "m3", "km3"],
            ["mg", "cg", "g", "dkg", "kg", "t"],
            ["ml", "cl", "dl", "l", "hl"],
            []]
valtok = [  [10, 10, 10 ,1000, 1],
            [100, 100, 100, 1000000, 1],
            [1000, 1000, 1000, 1000000000, 1],
            [10, 10, 10, 100, 1000, 1],
            [10, 10, 10, 100, 1]]
tipusId="";
egysegId="";
egysegId2="";
while tipusId!=0 or egysegId!=0 or egysegId2!=0:
    print("#"*40);
    #for elem in tipusok:
    #    print(elem)

    print("Mértékegységek típusok:")
    #Mértékegség típus kiírás
    for i,elem in enumerate(tipusok):
        print("\t",str(i+1)+":", elem);

    print("\t 0: Kilépés");
    print("#"*40);

    tipusId="";

    #Mértékegység típus bekérés
    while tipusId=="" or tipusId not in range(len(tipusok)+1):
        try:
            tipusId = int(input("Válassz!"));
            if  tipusId not in range(len(tipusok)+1):
                raise
        except:
            print("Nem jó! Válassz a listából!")
            
    #Ha a kilépést(0) választják akkor véget ér a program
    if tipusId==0:
        break
    
    print("#"*40)
    tipusId -=1
    print("Mértékegység típus:", tipusok[tipusId])

    print("Mértékegységek:")

    #Mértékegység  kiírása (Miből)
                    #if tipusId==5:
                    #    for e,elem in enumerate(egysegek[2]):
                    #        print("\t",str(e+1)+":",elem)
                    #    for b,elem2 in enumerate(egysegek[4]):
                    #        print("\t",str(b+6)+":",elem2)
                    #else:
    for i,elem in enumerate(egysegek[tipusId]):
        print("\t",str(i+1)+":", elem);

    print("\t 0: Kilépés");
    print("#"*40);

    egysegId="";

    #Mértékegység  bekérése (Miből)
    while egysegId=="" or egysegId not in range(len(egysegek[tipusId])+1):
        try:
            egysegId = int(input("Válaszd ki, hogy miből szeretnél átváltani!:"));
            if  egysegId not in range(len(egysegek[tipusId])+1):
                raise
        except:
            print("Nem jó! Válassz a listából!")
            
    #Ha a kilépést(0) választják akkor véget ér a program
    if egysegId==0:
        break
    
    print("#"*40)
    egysegId-=1
    print("Kívánt mértékegységből való átváltás:", egysegek[tipusId][egysegId])


    #Mértékegység kiírása (Mibe)
    for i,elem in enumerate(egysegek[tipusId]):
        print("\t",str(i+1)+":", elem);

    print("\t 0: Kilépés");
    print("#"*40);

    egysegId2="";

    #Mértékegység bekérése (Mibe)
    while egysegId2=="" or egysegId not in range(len(egysegek[tipusId])+1):
        try:
            egysegId2 = int(input("Válaszd ki, hogy mibe szeretnél átváltani!:"));
            if  egysegId2 not in range(len(egysegek[tipusId])+1):
                raise
        except:
            print("Nem jó! Válassz a listából!")
            
    #Ha a kilépést(0) választják akkor véget ér a program
    if egysegId2==0:
        break

    egysegId2-=1
    print("#"*40)
    print("Kívánt mértékegységbe váltás:", egysegek[tipusId][egysegId2])
    print("#"*40)


    szam=input("Írd be az átváltani kívánt mennyiséget!:")
    while szam.isdigit()==False:
        try:
            szam = input("Írd be az átváltani kívánt mennyiséget!:");
            if  szam.isdigit()==False:
                raise
        except:
            print("Nem jó! Számot írj be!")
    szam=float(szam)
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
    print("#"*40)

    print("Eredmény:", szam, egysegek[tipusId][egysegId], "=", eredmeny, egysegek[tipusId][egysegId2])


    #Házi: Csinosítás, számbekérésnél ellenőrzés hogy szám-e, while try, addig kell csinálni amig a tipusválasztónál a kilépést nem választjuk, (egészet egy while-ba)
