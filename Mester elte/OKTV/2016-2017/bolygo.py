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
    sor=1
    bolygok=[]
    bolygo=[]
    with open(argv[1],"r") as f:
        A,B,C=map(int,f.readline().split())
        ListaF=list(f)
        bolygok.append(list(map(vagas,ListaF[:A])))
        bolygok.append(list(map(vagas,ListaF[A:B+A])))
        bolygok.append(list(map(vagas,ListaF[B+A:C+B+A])))
        elet=[]
        while A!=B or A!=C:
            bolygok[2].append([])
            C+=1
        for bolygoI in range(2):
            if ellenorzes(bolygok[0][bolygoI],bolygok[1][bolygoI]):
                elet.append(setAlakitas(bolygok[0][bolygoI]).intersection(setAlakitas(bolygok[1][bolygoI])))
            elif ellenorzes(bolygok[0][bolygoI],bolygok[2][bolygoI]):
                elet.append(setAlakitas(bolygok[0][bolygoI]).intersection(setAlakitas(bolygok[2][bolygoI])))
            elif ellenorzes(bolygok[1][bolygoI],bolygok[2][bolygoI]):
                elet.append(setAlakitas(bolygok[1][bolygoI]).intersection(setAlakitas(bolygok[2][bolygoI])))
        print(elet)
                
main()