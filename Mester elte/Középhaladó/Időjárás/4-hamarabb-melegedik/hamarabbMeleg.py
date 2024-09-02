from sys import stdin,stdout

def main():
    kimenet=[100,-1]
    telepulesDb,napok=list(map(int,input().split()))
    for telepules,sor in enumerate(stdin):
        sor=list(map(int,sor.split()))
        for i,data in enumerate(sor):
            if i+2<len(sor) and data>sor[i+1]<sor[i+2]:
                if kimenet[0]>i+2:
                    kimenet[0]=i+2
                    kimenet[1]=telepules+1
    stdout.write(str(kimenet[1]))


main()
                
