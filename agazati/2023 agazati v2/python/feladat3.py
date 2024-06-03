class Hegy():
    def __init__(self,hegycsucs,hegyseg,magassag) -> None:
        self.hegycsucsnev=hegycsucs
        self.hegyseg=hegyseg
        self.magassag=magassag

    def labAtvalt(self):
        self.lab=str(round(self.magassag*3.280839895,2))

#1. feladat
f=open("hegyekMo.txt","r")
hegyek=[]
next(f)
for sor in f:
    vag=sor.strip().split(";")
    hegyek.append(Hegy(vag[0],vag[1],int(vag[2])))

f.close()

#2. feladat
print("2. feladat")
print("\tA hegycsúcsok száma: {}".format(len(hegyek)))

#3.feladat
atlagMagassag=0
for hegy in hegyek:
    atlagMagassag+=hegy.magassag

atlagMagassag=atlagMagassag/len(hegyek)

print("3. feladat")
print("\tA hegycsúcsok átlagos magassága: {}m".format(atlagMagassag))

#4. feladat
legalacsonyabb=0
temphegy=100000
for hegy in hegyek:
    if temphegy>hegy.magassag:
        temphegy=hegy.magassag
        legalacsonyabb=hegy.hegycsucsnev

print("4. feladat")
print("\tA legalacsonyabb csúcs: {}".format(legalacsonyabb))

#5. feladat
f=open("matra.txt","w",encoding="utf-8")

for hegy in hegyek:
    hegy.labAtvalt()
    f.write(hegy.hegycsucsnev+";"+str(hegy.lab)+"\n")

f.close()