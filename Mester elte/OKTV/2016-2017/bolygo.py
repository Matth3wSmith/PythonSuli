from sys import stdout,stdin,argv

def vagas(string):
    return list(map(int,string.strip().split()))

def ellenorzes(bolygoList1,bolygoList2) -> bool:
    if len(bolygoList1)==0 or len(bolygoList2)==0:
        return False
    return bolygoList2[0]<=bolygoList1[0]<=bolygoList2[1] or bolygoList2[0]<=bolygoList1[1]<=bolygoList2[1]

def setAlakitas(lista):
    return set(range(lista[0],lista[1]))

def main():
    #Jól működik kis adatokkal :)
    """#TODO: Matrix keszitese a beolvasott adatokbol
        #Életek intervalluma
    bolygo1,bolygo2,bolygo3=list(map(int,input().split()))
    bolygo1Elet=[list(map(int,input().split())) for __ in range(bolygo1)]
    bolygo2Elet=[list(map(int,input().split())) for __ in range(bolygo2)]
    bolygo3Elet=[list(map(int,input().split())) for __ in range(bolygo3)]
        #Maximum kikeresése
    maxElet=0
    for bolygo in [bolygo1Elet,bolygo2Elet,bolygo3Elet]:
        for egyElet in bolygo:
            if max(egyElet)>maxElet:
                maxElet=max(egyElet)
        #Az eletMatrixban előre telepakolom a lehetséges legnagyobb évig "0"-val, hogy már csak át kelljen írni "1"-re azt, ahol van élet
    eletMatrix=[[0 for __ in range(maxElet)] for __ in range(3)]

        #Időszakok átírása
    bolygok=[bolygo1Elet,bolygo2Elet,bolygo3Elet]
    for bolygoI in range(len(bolygok)):
        for egyIdo in bolygok[bolygoI]:
            evHossz=egyIdo[1]-egyIdo[0]+1
            for i in range(evHossz):
                eletMatrix[bolygoI][egyIdo[0]-1+i]=1
    print(eletMatrix)

    ###############################################################

    elet=[] #Ebben lesz eltárolva a végső időszak a kimenethez
    tempElet=[0,0] #Ideiglenes lista ami tárolja, hogy mikor van (egy időszakban) legalább két bolygón élet
    masodikAg=False
    harmadikAg=False
    negyedikAg=False

    for i in range(maxElet):
            #Megvizsgálja, hogy az első és második bolygón van-e élet, első esetet nézi, ha talál akkor másik ágon folytatja
        if eletMatrix[0][i]==1 and eletMatrix[1][i]==1 and not masodikAg and not harmadikAg and  not negyedikAg:
            tempElet=[i+1,i]
            masodikAg=True
            #harmadikAg=True
            #negyedikAg=True


        elif eletMatrix[0][i]==1 and eletMatrix[2][i]==1 and not masodikAg and not harmadikAg and  not negyedikAg:
            tempElet=[i+1,i]
            #masodikAg=True
            harmadikAg=True
            #negyedikAg=True

        elif eletMatrix[1][i]==1 and eletMatrix[2][i]==1 and not masodikAg and not harmadikAg and  not negyedikAg:
            tempElet=[i+1,i]
            #masodikAg=True
            #harmadikAg=True
            negyedikAg=True
        
        ##################################################################

            #Ha már talált életet, növeli annak idejét, ameddig mindkettő bolygón van élet
        if eletMatrix[0][i]==1 and eletMatrix[1][i]==1 :
            tempElet[1]+=1

            #Ha nem talált életet, vagy többé nincs egyszerre mindkét bolygón élet akkor eltárolja a meglévőt és nulláz

        ##################################################################

        elif eletMatrix[0][i]==1 and eletMatrix[2][i]==1 :
            tempElet[1]+=1
        
        ##################################################################

        elif eletMatrix[1][i]==1 and eletMatrix[2][i]==1:
            tempElet[1]+=1
        else:
            masodikAg=False
            harmadikAg=False
            negyedikAg=False
            if tempElet!=[0,0]:
                elet.append(tempElet)
            tempElet=[0,0]
        
        ##################################################################
    if tempElet!=[0,0]:
        elet.append(tempElet)"""

    bolygo1,bolygo2,bolygo3=list(map(int,input().split()))
    elet=[]
    tempElet=[0,0]
    bolygok=[bolygo1,bolygo2,bolygo3]
    bolygoElet=[[],[],[]]

    for bolygoI in range(len(bolygok)):
        for i in range(bolygok[bolygoI]):
            bolygoElet[bolygoI].append(list(map(int,input().split())))
    
    for i in range(len(bolygoElet[0])):
        pass

    stdout.write(str(len(elet))+"\n")
    for sor in elet:
        stdout.write(str(sor[0])+" "+str(sor[1])+"\n")
main()


