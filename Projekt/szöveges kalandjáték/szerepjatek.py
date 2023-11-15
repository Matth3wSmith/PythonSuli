#Lista kiíratás függvénye
def menu(lista):
    for i, elem in enumerate(lista):
        print("{} - {}".format(i+1, elem))

    valasztas = 0

    while (valasztas<1 or valasztas>len(lista)) and valasztas != 69:
        try:
            valasztas = int(input("Válassz egy számot a listából:"))
        except:
            pass

    return valasztas-1

#lista = ["Előre", "Hátra", "Jobbra", "Balra"]
#valasz = menu(lista);
#print(valasz, lista[valasz])


#Nyelv választás
nyelv=["Magyar", "English", "Deutsch", "Russian"]
nyelvId={"Magyar":"szovegHun","English":"szovegEng"}
print("Válassz nyelvet")
while True:
    nyelvValasztas=menu(nyelv)
    #print(nyelv[nyelvValasztas])
    if nyelv[nyelvValasztas] in nyelvId:
        break
    else:
        print("Sajnos ez a fordítás még nem készült el!")

if nyelvId[nyelv[nyelvValasztas]] == "szovegHun":
    import szovegHun as t
elif nyelvId[nyelv[nyelvValasztas]] == "szovegEng" : 
    import szovegEng as t


tortenet=[
        [
            1,#szál ID
            t.text["Megérkezel a kazamata bejáratához. Csikorogva kinyílik az ajtó és egy sötét, dohos folyosó fogad."], #szöveg szovehun fájlból választja ki a nyelvet
            [t.text["belépsz és gyyújtasz egy fáklyát"], t.text["besétálsz a sötétbe"]], #választái lehetőségek
            [3,2] #hova ugorjon
        ],
        [
            2,#szál ID
            t.text["Túl hideg van, halálra fagytál!"], #szöveg
            [t.text["újrakezdés"], t.text["kilépés"]], #választái lehetőségek
            [1,66] #hova ugorjon
        ],
        [
            3,#szál ID
            t.text["Gyújtasz egy fáklyát. Balra van egy nyitott ajtó, de a fény nem hatol be. Jobbra egy zárt, rozoga ajtó."], #szöveg
            [t.text["Jobb oldali ajtó"], t.text["Bal oldali ajtó"]], #választái lehetőségek
            [4,5] #hova ugorjon
        ],
        [
            4,#szál ID
            t.text["Megpróbálod kinyitni az ajtó. Nincs zárva, ezért lassan csikorogva kinyílik. Egy kobold van a szobában."], #szöveg
            [t.text["harc! (kockadobás)"], t.text["menekülés"]], #választái lehetőségek
            [2,3,4,66] #hova ugorjon
        ],
        [
            5,#szál ID
            t.text["Besétálsz a nyitott szobába, a fáklyád nem ér semmit, ezért nem látsz és belesétálsz egy medvecsapdába."], #szöveg
            [t.text["harc! (kockadobás)"], t.text["menekülés"]], #választái lehetőségek
            [7 if roll(12) else 9 if roll(12) else 8,6
             #győzelem          #] #hova ugorjon
        ],
        [
            6,#szál ID
            t.text["Gyáván megfutamodtál. A játék véget ért!"], #szöveg
            [t.text["újrakezdés"], t.text["kilépés"]], #választái lehetőségek
            [1,66] #hova ugorjon
        ],
        [
            7,#szál ID
            t.text["Nagyobbat dobtál mint az ellenfél, ezért csúnyán megverted!"], #szöveg
            [t.text[""], t.text[""]], #választái lehetőségek
            [2,6] #hova ugorjon
        ],
        [
            8,#szál ID
            t.text["Kevesebbet dobtál mint az ellenfél, ezért csúnyán megvert! Meghaltál!"], #szöveg
            [t.text["újrakezdés"], t.text["kilépés"]], #választái lehetőségek
            [1,66] #hova ugorjon
        ],
        [
            66,#szál ID
            t.text[], #szöveg
            [], #választái lehetőségek
            [] #hova ugorjon
        ],
    ]

szalId=1
while True:
    #temp=[]
    #for e in tortenet:
    #    temp.append(e[0])
    #másként listák ID kígyűjtése
    temp=[e[0] for e in tortenet]
    szalIndex=temp.index(szalId)

    print(tortenet[szalIndex][1])
    
    if tortenet[szalIndex][2]==[]:
        break

    menuPont = menu(tortenet[szalIndex][2])

    if menuPont == 68:
        break

    szalId=tortenet[szalIndex][3][menuPont]
        

print("The End")




