from sys import stdin,stdout
import math

def main():
    napSzam,K,L,F=list(map(int,stdin.readline().split()))
    napok=list(map(int,stdin.readline().split()))
    riadok=0
    riadoVan=False
    riadoLehet=0
    riadoTorles=0
    for i in range(0,napSzam):
        if not riadoVan:
            for k in range(K):
                if napok[i+k]>F:
                    riadoLehet+=1
                    
                else:
                    i=i+1
                    break
            if riadoLehet==K:
                riadok+=1
                riadoVan=True
            riadoLehet=0
        else:
            for k in range(L):
                if napok[i+k]<F:
                    
                    riadoTorles+=1
                else:
                    i=i+1
                    break
            if riadoTorles==L:
                riadoVan=False
            riadoTorles=0

    stdout.write(str(riadok))



main()