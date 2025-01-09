from sys import stdin,stdout
def main():
    rendelesek,napokSzama=list(map(int,stdin.readline().split()))
    napok=[]
    kezdoNapok=[]
    voltmar=[False] * rendelesek
    voltKicsi=[False] * rendelesek
    for sor in range(rendelesek):
        tempNapok=list(map(int,stdin.readline().split()))
        napok.append(tempNapok)
        kezdoNapok.append(tempNapok[0])

    kicsi=min(kezdoNapok)
    k=kezdoNapok.index(kicsi)
    lehet=[[napok[k]]]
    voltKicsi[k]=True
    kezdoNapok[k]=napokSzama+1
    def rendel(i,lehet):
        if i+1>=len(napok):
            kisebb=kezdoNapok.index(min(kezdoNapok))
            lehet.append([napok[kisebb]])
            return
        if napok[i][0]>lehet[-1][-1][1] and not voltmar[i]:
            lehet[-1].append(napok[i])
            voltmar[i]=True

        rendel(i+1,lehet)            
        print(lehet)



main()