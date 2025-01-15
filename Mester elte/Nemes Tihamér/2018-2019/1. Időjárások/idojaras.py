from sys import stdin,stdout

def main():
    napSzam,K,L=map(int,stdin.readline().split())
    napok=list(map(int,stdin.readline().split()))
    meleg=[]
    hideg=[]
    mindketto=[]
    for i in range(1,napSzam-1):
        if napok[i-1]<napok[i] and napok[i]>napok[i+1]:
            meleg.append(i)
            mindketto.append(i)
        if napok[i-1]>napok[i] and napok[i]<napok[i+1]:
            hideg.append(i)
            mindketto.append(i)
    kezdo=0
    melegSzamlalo=0
    hidegSzamlalo=0
    ossz=0
    for i in range(napSzam):
        if i in meleg:
            melegSzamlalo+=1
        if i in hideg:
            hidegSzamlalo+=1

        if melegSzamlalo>K and mindketto[0] in meleg:
            melegSzamlalo-=1
            kezdo=mindketto.pop(0)+1

        elif melegSzamlalo>K and mindketto[0] not in meleg:
            while melegSzamlalo>K:
                nap=mindketto.pop(0)
                if nap in meleg:
                    melegSzamlalo-=1
                else:
                    hidegSzamlalo-=1
                kezdo=nap+1
                
        elif hidegSzamlalo>L and mindketto[0] in hideg:
            hidegSzamlalo-=1
            kezdo=mindketto.pop(0)+1
        elif hidegSzamlalo>L and mindketto[0] not in hideg:
            while hidegSzamlalo>L:
                nap=mindketto.pop(0)
                if nap in meleg:
                    melegSzamlalo-=1
                else:
                    hidegSzamlalo-=1
                kezdo=nap+1

        if melegSzamlalo==K and hidegSzamlalo==L:
            ossz+=mindketto[0]+1-kezdo
    print(ossz)

main()
