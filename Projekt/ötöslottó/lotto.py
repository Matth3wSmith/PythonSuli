import random
bekert = ""
while bekert != 0:
    valaszto=["Ötöslottó", "Hatoslottó", "Skandináv lottó","Totó"]
    for i,elem in enumerate(valaszto):
        print(i+1,":", elem)
    print("0 : Kilépés")
    print("#"*40)
    bekert = int(input("Adj meg egy számot a fentiek közül:"))-1;
    if bekert+1 == 0:
        break
    while bekert not in range((len(valaszto))):
        try:
            bekert = int(input("Adj meg egy számot a fentiek közül:"))-1;
            if  bekert not in range(len(valaszto)):
                raise
        except:
            print("Nem jó! Válassz a listából!")
    print("#"*40)
    bekert+=1
    def kiiratas(lista):
            for i in range(len(lista)):
                print(lista[i]);
    if bekert == 1:
        #ÖTÖSLOTTÓ
        otosLista = []

        while len(otosLista)<= 4:
            randomSzam = random.randint(1,90);
            if randomSzam not in otosLista:
                otosLista.append(randomSzam)

        print("A gép áltál sorsolt Ötöslottó számok:")
        kiiratas(otosLista)
        print("#"*40)
    elif bekert == 2:
        #HATOSLOTTÓ
        hatosLista = []

        while len(hatosLista)<= 5:
            randomSzam = random.randint(1,45);
            if randomSzam not in hatosLista:
                hatosLista.append(randomSzam)

        print("A gép által sorsolt Hatoslottó számok:")
        kiiratas(hatosLista)
        print("#"*40)
    elif bekert == 3:
        #SKANDINÁV LOTTÓ

        skandiLista = []

        while len(skandiLista)<= 6:
            randomSzam = random.randint(1,35);
            if randomSzam not in skandiLista:
                skandiLista.append(randomSzam)
                
        print("A gép által sorsolt Skandináv lottó számok:")
        kiiratas(skandiLista)
        print("#"*40)
    elif bekert == 4:
        #toto
        toto=["1","2","x"];
        toto2=[];
        while len(toto2)<= 13:
            index = random.randint(0,2);
            toto2.append(toto[index]);
        print("A gép által sorsolt Totó számok:")
        for i,elem in enumerate(toto2[:-1]):
            print(i+1,':',elem)
        print("13+1 :",toto2[-1])
        print("#"*40)
    elif bekert == 0:
        break
