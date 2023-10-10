szoveg = "."
szovegLista = []
i = 0
while szoveg != "":
    szoveg = str(input("Adj meg egy szót!"))
    if szoveg == "":
        break
    szovegLista.append(szoveg)
    while szoveg.isdigit()==True:
        try:
            szoveg = str(input("Adj meg egy szót! Ha nem szeretnél többet megadni akkor nyomj egy entert!"))
            if  szoveg.isdigit()==True:
                    raise
        except:
            print("Nem jó! Szöveget írj be!")
    i+=1
    

print("A szavaid amiket bediktáltál:",szovegLista)
#Lista lemásolása későbbre
szovegLista2 = szovegLista.copy()
print(szovegLista2)
#Kiiratás abc sorrendben
szovegLista.sort()
print("Betűrendbe rendezve:", szovegLista)

#Utolsó 3 elem kiiratása
print("Lista utolsó 3 eleme:",szovegLista[(len(szovegLista)-3):len(szovegLista)])

#Eredeti utolsó 3 elemének sorba rendezése
szovegLista2 = szovegLista2[(len(szovegLista2)-3):len(szovegLista2)]
szovegLista2.sort()
print("Eredeti lista utolsó 3 elemének sorba rendezése:", szovegLista2)

