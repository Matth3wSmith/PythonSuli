class Hianyzo():
    def __init__(self,nev,hiany,datum) -> None:
        self.nev=nev
        self.hianyzas=hiany
        self.datum=datum

        honap=int(datum.split()[0])
        nap=int(datum.split()[1])
        self.nap=hetnapja(honap, nap)
    def hianyzasok(self):
        igazolt=self.hianyzas.count("X")
        igazolatlan=self.hianyzas.count("I")
        return igazolt,igazolatlan

def hetnapja(honap, nap):
    napnev=["vasarnap","hetfo", "kedd", "szerda", "csutortok", "pentek", "szombat"]
    napszam=[0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 335]
    napsorszam=(napszam[honap-1]+nap) % 7
    hetnapja=napnev[napsorszam]
    return hetnapja


hianyzok=[]
datum=""
adatok=[]
f=open("naplo.txt","r")
for sor in f:
    adatok.append(sor.strip())


for i in range(len(adatok)):
    if adatok[i][0]=="#":
        datum=adatok[i].strip().split("#")[1]
        continue
    vag=adatok[i].strip().split(" ")
    hianyzok.append(Hianyzo(vag[0]+" "+vag[1],vag[2],datum))
f.close()


#2. feladat
print("2. feladat")
print("A naplóban {} bejegyzés van.".format(len(hianyzok)))

#3. feladat
igazolt=0
igazolatlan=0
for hianyzo in hianyzok:
    tempIgazolt,tempIgazolatlan = hianyzo.hianyzasok()
    igazolt+=tempIgazolt
    igazolatlan+=tempIgazolatlan

print("3. feladat")
print("Az igazolt hiányzások száma {}, az igazolatlanoké {} óra".format(igazolt,igazolatlan))

#5. feladat
print("5. feladat")
honap=int(input("A hónap sorszáma: "))
nap=int(input("A nap sorszáma: "))
print("Azon a napon {} volt.".format(hetnapja(honap,nap)))

#6. feladat
print("6. feladat")
tanitasiNap=input("A nap neve: ")
oraSzama=int(input("Az óra sorszáma: "))
hianyzasOra=0
for hianyzo in hianyzok:
    if hianyzo.nap==tanitasiNap and hianyzo.hianyzas[oraSzama-1]!="O":
        hianyzasOra+=1
print("Ekkor összesen {} óra hiányzás történt.".format(hianyzasOra))

#7. feladat
hianyzasokDict={}
for hianyzo in hianyzok:
    if hianyzo.nev not in hianyzasokDict.keys():
        hianyzasokDict[hianyzo.nev]=len(hianyzo.hianyzas)-hianyzo.hianyzas.count("O")
    else:
        hianyzasokDict[hianyzo.nev]+=len(hianyzo.hianyzas)-hianyzo.hianyzas.count("O")

tempHiany=0
tempHianyNev=0
legtobbHianyzok=[]
for nev in hianyzasokDict:
    if tempHiany<hianyzasokDict[nev]:
        tempHiany=hianyzasokDict[nev]
        tempHianyNev=nev
    elif tempHiany==hianyzasokDict[nev]:
        legtobbHianyzok.append(tempHianyNev)
        legtobbHianyzok.append(nev)

print("7. feladat")
print("A legtöbbet hiényzó tanulók: {} {}".format(legtobbHianyzok[0],legtobbHianyzok[1]))

