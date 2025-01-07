from sys import stdin,stdout
def main():
    rendelesek,napokSzama=list(map(int,stdin.readline().split()))
    napok=[]
    kezdoNapok=[]
    for sor in range(rendelesek):
        tempNapok=list(map(int,stdin.readline().split()))
        napok.append(tempNapok)
        kezdoNapok.append(tempNapok[0])
    
    kicsi=min(kezdoNapok)
    lehet=[[napok[kezdoNapok.index(kicsi)]]]
    for rendeles in napok:
        if rendeles[0]>lehet[-1][-1][1]:
            lehet[-1].append(rendeles)
    print(lehet)



main()