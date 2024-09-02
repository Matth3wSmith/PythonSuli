from sys import stdin,stdout

def main():
    sor,oszlop=list(map(int,input().split()))
    kep=[]
    for sor in stdin:
        kep.append(sor.split()[0])
    print(kep)
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
    
            



main()