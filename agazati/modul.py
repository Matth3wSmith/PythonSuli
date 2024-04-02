def szamBekeres():
    szam=0
    szamlalo=1
    halmazA=[]
    halmazB=[]
    #'A' halmaz
    while szam!="":
        szam=input("'A' halmaz {}. eleme: ".format(szamlalo))
        
        while szam in halmazA:
            print("HIBA! a(z) {} már benne van a(z) 'A' halmzaban!".format(szam))
            szam=input("'A' halmaz {}. eleme: ".format(szamlalo))
        if szam=="":
            break
        halmazA.append(szam)
        szamlalo+=1

    print("'A' halmza feltöltése befejeződött!\n")
    szamlalo=1
    szam=0
    #'B' halmaz
    while szam!="":
        szam=input("'B' halmaz {}. eleme: ".format(szamlalo))
        
        while szam in halmazB:
            if szam in halmazB:
                print("HIBA! a(z) {} már benne van a(z) 'B' halmzaban!".format(szam))
                szam=input("'B' halmaz {}. eleme: ".format(szamlalo))
        if szam=="":
            break
        halmazB.append(szam)
        szamlalo+=1
    print("'B' halmza feltöltése befejeződött!\n")

    for i,elem in enumerate(halmazA):
        halmazA[i]=int(elem)
    for i,elem in enumerate(halmazB):
        halmazB[i]=int(elem)
    return halmazA,halmazB

def metszet(halmaz1,hamlaz2):
    metszet=[]
    for elem in halmaz1:
        if elem in hamlaz2:
            metszet.append(elem)
    return metszet