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


tortenet=[
        [
            1,#szál ID
            "Reggel felébredtem. Mit tegyek?", #szöveg
            ["fogmosás", "reggeli", "öltözés"], #választái lehetőségek
            [2,3,4] # hova ugorjon
        ],
        [
            2,#szál ID
            "Elmegyek fogat mosni. Sikálom rendesen, ahogy kell!", #szöveg
            ["fogmosás", "reggeli", "öltözés"], #választái lehetőségek
            [2,3,4] # hova ugorjon
        ],
        [
            3,#szál ID
            "Kellene valamit enni! Anya csinált valamit? Nézzük meg!", #szöveg
            ["fogmosás", "reggeli", "öltözés"], #választái lehetőségek
            [2,3,4] # hova ugorjon
        ],
        [
            4,#szál ID
            "Kissé hűvös van, kellene valami ruha. \nFelveszek egy nadrágot, meg egy pólót!", #szöveg
            ["fogmosás", "reggeli", "öltözéa","66-os parancs"], #választái lehetőségek
            [2,3,4,66] # hova ugorjon
        ],
        [
            66,#szál ID
            "Véde mindennek....", #szöveg
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




