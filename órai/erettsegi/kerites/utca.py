class Telek:
    def __init__(self,sor) -> None:
        vag=sor.split(" ")
        self.oldal=int(vag[0])
        self.szelesseg=int(vag[1])
        self.szin=vag[3]
        self.hazszam=0

telkek=[]
parosParatlan=[0,-1]
f=open("kerites.txt","r")
for sor in f:
    telkek.append(Telek(sor))
    parosParatlan[telkek[-1].oldal]+=2
    telkek[-1].hazszam=parosParatlan[telkek[-1].oldal]
f.close()

#2. feladat
print("2.feladat")
print("Az eladott telkek száma: {}".format(len(telkek)))

#3. feladat
print("3. feladat")
if telkek[-1].oldal==0:
    print("A páros oldalon adták el az utolsó telket")
else:
    print("A páratlan oldalon adták el az utolsó telket")
print("Az utolsó telek házszáma: {}".format(telkek[-1].hazszam))

#4. feladat
oldalSzerint=[[],[]]

