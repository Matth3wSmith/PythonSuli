#Gyártó: Kovács Máté

class LabdaMenet:
    def __init__(self, labda) -> None:
        self.labdamenet=labda

class Játék:
    def __init__(self,fogado,adogato,allas) -> None:
        self.fogado=fogado
        self.adogato=adogato
        self.allas=allas

    def Hozzáad(self,labdamenet):
        self.allas+=labdamenet

    def NyertLabdamenetekSzáma(self,jatekos):
        nyert=0
        for menet in self.allas:
            if menet==jatekos:
                nyert+=1
        return nyert

    def JátékVége(self) -> bool:
        nyertAdogató=0
        nyertFogadó=0
        különbség=0
        nyertAdogató= self.NyertLabdamenetekSzáma('A')
        nyertFogadó= self.NyertLabdamenetekSzáma('F')
        különbség=abs(nyertAdogató-nyertFogadó)
        return(nyertAdogató>=4 or nyertFogadó >=4) and különbség>=2   

#2.feladat
labdamenetek=[]
f=open("labdamenetek5.txt","r")
for sor in f:
    labdamenetek.append(LabdaMenet(sor.strip()))
f.close()

""#3. feladat
osszMenet=len(labdamenetek)
print("3.feladat: Labdamenetek száma: {}".format(osszMenet))

#4. feladat
adogatoNyert=0
for menet in labdamenetek:
    if menet.labdamenet=="A":
        adogatoNyert+=1

print("4. feladat: Az adogató játékos {}%-ban nyerte meg a labdamenetek.".format(100/osszMenet*adogatoNyert))

#5. feladat
legHosszabb=0
tempHossz=0
for menet in labdamenetek:
    if menet.labdamenet=="A":
        tempHossz+=1
    elif tempHossz>legHosszabb:
        legHosszabb=tempHossz
        tempHossz=0
    else:
        tempHossz=0

print("5. feladat: Leghosszabb sorozat: {}".format(legHosszabb))

#7. feladat
PróbaJáték=Játék("Isner","Mahut","FAFAA")
PróbaJáték.Hozzáad("A")
print("7. feladat: A próba játék")
print("\tÁllás: {}".format(PróbaJáték.allas))
if PróbaJáték.JátékVége:
    print("\tBefejeződött a játék: {}".format("Igen"))
else:
    print("\tBefejeződött a játék: {}".format("Nem"))

#8. feladat
játékok=[]
jatekosok=["Mahut","Isner"]
index=1
tempJáték=Játék("Mahut","Isner","")
for menet in labdamenetek:
    tempJáték.Hozzáad(menet.labdamenet)
    if tempJáték.JátékVége():
        játékok.append(tempJáték)
        if index==0:
            tempJáték=Játék("Mahut","Isner","")
            index=1
        elif index==1:
            tempJáték=Játék("Isner","Mahut","")
            index=0


#9. feladat
nyeresekDict={"Mahut":0,"Isner":0}
for jatek in játékok:
    if jatek.NyertLabdamenetekSzáma("A")>jatek.NyertLabdamenetekSzáma("F"):
        nyeresekDict[jatek.adogato]+=1
    else:
        nyeresekDict[jatek.fogado]+=1
    
print("9. feladat: Az 5. játszma végeredménye:")
print("\tMahut: {}".format(nyeresekDict["Mahut"]))
print("\tIsner: {}".format(nyeresekDict["Isner"]))