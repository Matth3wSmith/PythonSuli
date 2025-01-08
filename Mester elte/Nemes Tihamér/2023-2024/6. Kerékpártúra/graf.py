from sys import stdin,stdout
import sys


adatok=""""8 16 2
1 3
2 1
2 5
5 4
5 1
5 6
4 3
4 7
4 1
3 8
3 7
6 2
6 4
6 7
7 8
8 3"""
#ADATOK BETÖLTÉSE GYORSABBAN


def utvonalVissza(kezdo,celpont,utvonal=[]):
    utvonal+=[kezdo]

    if kezdo==celpont:
        return [utvonal]
    if pontok[kezdo]==[]:
        return []

    utvonalak=[]
    for pont in pontok[kezdo]:
        if pont not in utvonal:
            #print(f"aktualis csucs: {kezdo} kovetkezo pont: {pont} jelenelegi utvonal: {utvonal} eddigiek: {utvonalak}")
            ujUtvonal=utvonalVissza(pont,celpont,utvonal)
            for ut in ujUtvonal:
                utvonalak.append(ut)

                i = utvonal.index(kezdo)
                utvonal=utvonal[:i+1]

    return utvonalak


def utvonalKeres(kezdo,celpont,utvonal=[],vissza=False):
    utvonal+=[kezdo]

    if kezdo==celpont:
        return [utvonal]
    
    if pontok[kezdo]==[]:
        return []

    utvonalak=[]
    for pont in pontok[kezdo]:
        if pont not in utvonal:
            #print(f"aktualis csucs: {kezdo} kovetkezo pont: {pont} jelenelegi utvonal: {utvonal} eddigiek: {utvonalak}")
            #print(visszajutas[pont],[pont])
            if visszajutas[pont]:
                #print(visszajutas)
                ujUtvonal=utvonalKeres(pont,celpont,utvonal,vissza)
                for ut in ujUtvonal:
                    utvonalak.append(ut)

                i = utvonal.index(kezdo)
                utvonal=utvonal[:i+1]
            elif pont==celpont:
                return utvonal



    
    return utvonalak

def main():
    pontSzam,szakaszSzam,kezdopont=list(map(int,stdin.readline().split()))

    global pontok
    pontok=[[] for __ in range(pontSzam+1)]

    global visszajutas
    visszajutas=[]
    visszajutas=visszajutas+[False]*(pontSzam+1)

    for i in range(szakaszSzam):
        sor=list(map(int,stdin.readline().split()))
        pontok[sor[0]].append(sor[1])

    for i in range(1,pontSzam+1):
        if i!=kezdopont:
            visszajutas[i]=utvonalVissza(i,kezdopont,utvonal=[])!=[]
    
    #print(visszajutas)
    veg=[]
    for i in range(1,pontSzam+1):
        if i!=kezdopont:
            if utvonalKeres(kezdopont,i,utvonal=[])!=[]:
                veg.append(i)
    
    stdout.write(str(len(veg))+"\n")
    stdout.write(" ".join(map(str,veg)))


main()