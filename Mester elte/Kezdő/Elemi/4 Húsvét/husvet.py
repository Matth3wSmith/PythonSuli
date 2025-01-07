from sys import stdin,stdout
honapDict={"januar":31,
           "februar":28,
           "marcius":31,
           "aprilis":30,
           "majus":31,
           "junius":30}

napokDict={1:"hetfo",
       2:"kedd",
       3:"szerda",
       4:"csutortok",
       5:"pentek",
       6:"szombat",
       7:"vasarnap"}

honapok=list(honapDict.keys())
def holdtolte(nap,idoszak,honap):
    return [nap+29-honapDict[honap], "du" if idoszak=="de" else "de" , honapok[honapok.index(honap)+1]]
def main():
    ev=int(input())
    elsoNap=int(input())
    holdtoltek=[[int(input()),input(),"januar"]]
    #print(ev,elsoNap,elsoHoldT)
    while True:
        holdtoltek.append(holdtolte(holdtoltek[-1][0],holdtoltek[-1][1],holdtoltek[-1][2]))
        if holdtoltek[-1][-1]=="marcius" and holdtoltek[-1][0]>=21 or holdtoltek[-1][-1]=="aprilis":
            break
    nap=0
    #Husvet
    for honap in honapDict.keys():
        if honap==holdtoltek[-1][-1]:
            nap+=holdtoltek[-1][0]
            break
        nap+=honapDict[honap]
    nap=napokDict[nap%7+elsoNap-1]
    husvet=[[holdtoltek[-1][-1],holdtoltek[-1][0]]]

    while nap!="vasarnap":
        nap=napokDict[list(napokDict.values()).index(nap)+2]
        husvet[0][-1]+=1

    #Ha husvet hetfo tullep a honapon
    if husvet[0][-1]+1>honapDict[husvet[0][0]]:
        ujHonap=honapok[honapok.index(husvet[0][0])+1]
        ujNap=husvet[0][-1]+1-honapDict[ujHonap]
        husvet.append([ujHonap,ujNap])
    else:
        husvet.append([husvet[0][0],husvet[0][-1]+1])
    print(husvet)

    #Punkosd
    kovihonap=honapok.index(husvet[0][0])+1
    punkosdVasarnap=(husvet[0][-1]+7*7)-honapDict[honapok[kovihonap]]
    honap=honapok[kovihonap]

    if punkosdVasarnap > honapDict[honapok[kovihonap+1]]:
        punkosdVasarnap-=honapDict[honapok[kovihonap+1]]
        honap=honapok[kovihonap+1]
    
    punkosd=[[honap,punkosdVasarnap+1],[honap,punkosdVasarnap+2]]
    print(punkosd)

main()