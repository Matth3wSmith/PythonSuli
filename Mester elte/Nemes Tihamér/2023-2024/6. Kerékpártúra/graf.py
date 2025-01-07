from sys import stdin,stdout
pontok=[]
def utvonalVissza(pontok,kezdo,celpont,utvonal=[]):
    utvonal+=[kezdo]

    if kezdo==celpont:
        return [utvonal]
    
    if pontok[kezdo]==[]:
        return []

    utvonalak=[]
    for pont in pontok[kezdo]:
        if pont not in utvonal:
            print(f"aktualis csucs: {kezdo} kovetkezo pont: {pont} jelenelegi utvonal: {utvonal} eddigiek: {utvonalak}")
            ujUtvonal=utvonalVissza(pontok,pont,celpont,utvonal)
            for ut in ujUtvonal:
                utvonalak.append(ut)


                i = utvonal.index(kezdo)
                utvonal=utvonal[:i+1]
    return utvonalak

def utvonalKeres(pontok,kezdo,celpont,indulas=0,utvonal=[]):
    utvonal+=[kezdo]

    if kezdo==celpont:
        return [utvonal]
    
    if pontok[kezdo]==[]:
        return []

    utvonalak=[]
    for pont in pontok[kezdo]:

        if pont not in utvonal:
            print(f"aktualis csucs: {kezdo} kovetkezo pont: {pont} jelenelegi utvonal: {utvonal} eddigiek: {utvonalak}")
            ujUtvonal=utvonalKeres(pontok,pont,celpont,indulas,utvonal)
            for ut in ujUtvonal:
                utvonalak.append(ut)

            i = utvonal.index(kezdo)
            utvonal=utvonal[:i+1]

    
    return utvonalak

def main():
    pontSzam,szakaszSzam,kezdopont=list(map(int,stdin.readline().split()))
    pontok=[[] for __ in range(pontSzam+1)]
    for i in range(szakaszSzam):
        sor=list(map(int,stdin.readline().split()))
        pontok[sor[0]].append(sor[1])
    
    print(utvonalKeres(pontok,kezdopont,5,kezdopont))


main()