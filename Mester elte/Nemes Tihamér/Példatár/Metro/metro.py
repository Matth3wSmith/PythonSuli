from sys import stdin,stdout

def main():
    ido,lepcsoHossz,kapacitas,metro,utasSzam=map(int,stdin.readline().split())
    utasok={i+1:0 for i in range(ido)}
    for __ in range(utasSzam):
        utas=int(stdin.readline())
        utasok[utas]+=1
    print(utasok)
    leszallok=list(map(int,stdin.readline().split()))
    utasfelul=0
    utasalul=0
    utasTavoz=0
    felszallas=[]
    lepcsonle=[0 for __ in range(lepcsoHossz+1)]
    lepcsonfel=[0 for __ in range(lepcsoHossz+1)]
    for i in range(1,ido+1):
        if utasalul+utasTavoz<kapacitas:
            #Ha vannak a lepcson akkor leért az első
            utasalul+=lepcsonle[-1]
            lepcsonle.pop(-1)
            #Ha vannak a lepcson akkor felert az első
            lepcsonfel.pop(-1)
            #Ha van felül utas és nem telt meg a lepcso
            if utasfelul!=0 and len(lepcsonle)!=lepcsoHossz+1:
                if utasfelul==1:
                    lepcsonle.insert(0,1)
                    utasfelul=0
                else:
                    lepcsonle.insert(0,2)
                    utasfelul-=2
            #Ha van alul varakozo utas es a lepcsofel nem telt meg
            if utasTavoz!=0 and len(lepcsonle)!=lepcsoHossz+1:
                if utasTavoz==1:
                    lepcsonfel.insert(0,1)
                    utasTavoz=1
                else:
                    lepcsonfel.insert(0,2)
                    utasTavoz-=2

            #Ha megjött a metro hozzaadjuk oket az utasaulul-hoz és a lent levoket a metrora rakjuk
            if metro==i:
                if utasalul!=0:
                    felszallas.append(utasalul)
                utasTavoz+=leszallok[0]
                leszallok.pop(0)
                metro+=metro

            #Ha van utas az akutális időben hozzaadjuk az utasfelul-höz
            if utasok[i]!=0:
                utasfelul+=utasok[i]
        else:
            break
    print(felszallas)


main()