from sys import stdin,stdout


def vizsgalat(x,y,sor,oszlop,kep):
    #alul
    x1=sor-(x-1)
    y2=oszlop-(y-1)

    alul=kep[x1][y]==1

def main():
    sor,oszlop=list(map(int,stdin.readline().split()))
    kep=[]
    for sor in stdin:
        print(sor)
        kep.append(sor.split()[0])
    #print(kep)
    maxPont=[0,0]
    minPont=[]
    minPontBool=False
    #Legnagyobb és legkisebb x- és y-koordináta
    for i in range(len(kep)):
        for k in range(len(kep[i])):
           if int(kep[i][k])==1:
                if not minPontBool:
                    minPont=[i,k]
                    minPontBool=True
                elif i>maxPont[0] or k>maxPont[1]:
                    maxPont=[i,k]
    
    #TODO: függévny készitése ami megnézi hogy a kep egyik oldalan egy pontnak meg van e párj a kép másik oldalán
    #p: feher
    #z: fekete
    #k: nem lehet eldönteni
    kepSor=maxPont[0]+1
    kepOszlop=maxPont[1]+1

    



main()