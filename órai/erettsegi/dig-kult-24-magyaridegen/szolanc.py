szavak=[]
szo=input("1. szó: ")

while True:
    if len(szo)==6:
        if len(szavak)==0:
            szavak.append(szo)

        elif szavak[-1][-1]==szo[0]:
            szavak.append(szo)
        else:
            print("Nem illeszkedett!")
            break
        szo=input("{}. szó: ".format(len(szavak)+1))
    else:
        print("A karakterek száma téves!")
        break

print("\nHelyes lépések száma: {}".format(len(szavak)))
szintDict={
    "kezdo":list(range(3)),
    "közepes":list(range(3,6)),
    "haladó":6
}
print(szintDict)
for szint in szintDict:
    if len(szavak)<6:
        if len(szavak) in szintDict[szint]:
            print("Szint: {}".format(szint))
            break
    else:
        print("Szint: {}".format("nehéz"))
        break
