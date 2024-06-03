class Zene():
    def __init__(self,helyezes,cim,eloado,elozo,legjobb,het) -> None:
        self.helyezes=int(helyezes)
        self.cim=cim
        self.eloado=eloado
        self.elozo=elozo
        self.legjobb=int(legjobb)
        self.het=int(het)
    
    def uj(self):
        return self.elozo=="-" and self.helyezes==self.legjobb and self.het==1

f=open("billboard.csv")

#1.feladat
zenek=[]
next(f)
for sor in f:
    vag=sor.strip().split(";")
    zenek.append(Zene(vag[0],vag[1],vag[2],vag[3],vag[4],vag[5]))
f.close()

#2. feladat
print("2. feladat")
kertPozicio=int(input("\tKérek egy pozíciót: "))
kertZene=0
for zene in zenek:
    if zene.helyezes==kertPozicio:
        kertZene=zene
print("\tA lista {}. helyén szereplő dal: {}:{}".format(kertPozicio,kertZene.eloado,kertZene.cim))

#3. feladat
uj=0
for zene in zenek:
    if zene.uj():
        uj+=1

print("3. feladat")
print("\tA héten {} új belépő volt.".format(uj))

#4. feladat
eloadoDict={}
for zene in zenek:
    if zene.eloado not in eloadoDict.keys():
        eloadoDict[zene.eloado]=1
    else:
        eloadoDict[zene.eloado]+=1

print("4. feladat")
legtobbEloado=max(eloadoDict.values())
for eloado in eloadoDict:
    if eloadoDict[eloado]==legtobbEloado:
        print("\tA legtöbbet szereplő előadó(k): {}".format(eloado))

#5. feladat
f=open("eloadok.txt","w")

for eloado in eloadoDict:
    f.write(eloado+"\n")

f.close()