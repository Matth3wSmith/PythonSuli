from sys import stdin,stdout

def main():
    kiement=[]
    telepules,napok=list(map(int,input().split()))


    sor=list(map(int,input().split()))
    elozoFok=sor[0]
    kapcs=0
    elozo=False
    for i in range(1,len(sor)):
        if sor[i]<elozoFok:
            kiement.append(i+1)
            elozoNap=i
            elozo=True
        elif not sor[i]<elozoFok and elozo:
            elozoFok=sor[i]
            break
        elozoFok=sor[i]

    for sor in stdin:
        sor=list(map(int,sor.split()))
        for i,fok in enumerate(sor,elozoNap):
            if fok<elozoFok:
                kiement.append(i+1)
                elozoFok=fok
                elozoNap=i
            
    kiement.sort()
    stdout.write(str(len(kiement))+" "+" ".join(list(map(str,kiement))))
main()