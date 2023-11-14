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
            t.text[""], #szöveg szovehun fájlból választja ki a nyelvet
            [t.text["fogmosás"], t.text["reggeli"], t.text["öltözés"]], #választái lehetőségek
            [2,3,4] # hova ugorjon
        ],
        [
            2,#szál ID
            t.text["Elmegyek fogat mosni. Sikálom rendesen, ahogy kell!"], #szöveg
            [t.text["fogmosás"], t.text["reggeli"], t.text["öltözés"]], #választái lehetőségek
            [2,3,4] # hova ugorjon
        ],
        [
            3,#szál ID
            t.text["Kellene valamit enni! Anya csinált valamit? Nézzük meg!"], #szöveg
            [t.text["fogmosás"], t.text["reggeli"], t.text["öltözés"]], #választái lehetőségek
            [2,3,4] # hova ugorjon
        ],
        [
            4,#szál ID
            t.text["Kissé hűvös van, kellene valami ruha. \nFelveszek egy nadrágot, meg egy pólót!"], #szöveg
            [t.text["fogmosás"], t.text["reggeli"], t.text["öltözés"],t.text["66-os parancs"]], #választái lehetőségek
            [2,3,4,66] # hova ugorjon
        ],
        [
            66,#szál ID
            t.text["Véde mindennek...."], #szöveg
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




