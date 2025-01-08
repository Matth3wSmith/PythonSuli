from sys import stdin, stdout
import sys
sys.setrecursionlimit(20000)
def melysegi(kezdo,latogatott):

    if kezdo in latogatott:
        return
    
    latogatott.add(kezdo)

    for szomszed in graf[kezdo]:
        melysegi(szomszed,latogatott)

    return latogatott


def melysegiVissza(kezdo,latogatott):

    if kezdo in latogatott:
        return
    
    latogatott.add(kezdo)

    for szomszed in graf2[kezdo]:
        melysegiVissza(szomszed,latogatott)

    return latogatott


def main():
    pontokSzama,szakaszSzam,kezdopont=list(map(int,stdin.readline().split()))
    global graf,graf2
    graf=[[] for _ in range(pontokSzama+1)]
    graf2=[[] for _ in range(pontokSzama+1)]

    for i in range(szakaszSzam):
       
       honnan,hova=list(map(int,stdin.readline().split()))
       #print(honnan,hova)
       graf[honnan].append(hova)
       graf2[hova].append(honnan)


    #print(graf)
    #print(graf2)
    utvonal=melysegi(kezdopont,set())
    utvonal.discard(kezdopont)
    #print(utvonal)
    utvonalakVissza=[]
    """for i in range(pontokSzama):
        utvonal=melysegi(i+1,set())
        utvonal.discard(i+1)
        utvonalak.append(utvonal)"""
    
    eredmeny=[]
    for i in range(pontokSzama):
        temputvonal=melysegiVissza(i+1,set())
        temputvonal.discard(i+1)
        utvonalakVissza.append(temputvonal)
    
    for pont in utvonal:
        elotteLevoCsucsok=graf2[pont]
        #print(pont,elotteLevoCsucsok)
        for i in elotteLevoCsucsok:
            tempUtvonal=melysegi(i,set())
            #print("Valamit",i, tempUtvonal)
            if kezdopont in tempUtvonal:
                
                #print("Jó célpont",pont)
                eredmeny.append(pont)
                break

    print(eredmeny)



main()