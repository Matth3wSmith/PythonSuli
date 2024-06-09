from sys import stdin,stdout

def main():
    atlag=0
    telepulesDb,napDb=list(map(int,input().split()))
    telepulesek=[0]
    for sor in stdin:
        telepulesek[0]+=1
        sor=list(map(int,sor.split()))
        atlag=sum(sor)/napDb
        feletti=0
        for nap in sor:
            if nap>atlag:
                feletti+=1
        if feletti>len(sor)-feletti:
            telepulesek.append(telepulesek[0])
    stdout.write(str(len(telepulesek)-1)+" "+" ".join(list(map(str,telepulesek[1:]))))
main()