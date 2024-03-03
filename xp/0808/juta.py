#Gyártó Kovács Máté

class Dolgozok():
    dolgozokLista=[]

    def __init__(self,azonosit,nev,anyjaNev,telepules,cim,fizetes,jutalom,belepes,szuletes,szuletesHely):
        self.azonosit=azonosit
        self.nev=nev
        self.anyjaNev=anyjaNev
        self.telepules=telepules
        self.cim=cim
        self.fizetes=fizetes
        self.jutalom=jutalom
        self.belepes=belepes
        self.szuletes=szuletes
        self.szuletesHely=szuletesHely
        self.dolgozokLista.append(self)
    #Jutalom összeg kiszámolás
    def jutalomSum(self):
        jutalomOsszeg=0
        for dolgozo in self.dolgozokLista:
            jutalomOsszeg+=dolgozo.jutalom
        return jutalomOsszeg
    #Fizetések átlagának kiszámolása
    def fizetesAtlag(self):
        atlagOssz=0
        dolgozokSzama=len(self.dolgozokLista)
        for dolgozo in self.dolgozokLista:
            atlagOssz+=dolgozo.fizetes
        atlag=atlagOssz/dolgozokSzama
        return atlag
    #Vizsgálat van e recski dolgozó
    def recskiDolgozo(self):
        k=0
        for dolgozo in self.dolgozokLista:
            if dolgozo.telepules=="Recsk":
                k+=1
        if k>0:
            return "Van recski dolgozó"
        else:
            return "Nincs recski dolgozó"
                
    #Vizsgálat hány tatai dolgozó van
    def tataiDolgozo(self):
        k=0
        for dolgozo in self.dolgozokLista:
            if dolgozo.telepules=="Tata":
                k+=1
        return k

#Dolgzók beolvasása
f=open("dolgozok.txt","r",encoding="utf-8")
adatok=[]
for sor in f:
    g=sor.strip().split(";")
    adatok.append(g)

f.close()

#print(adatok)
#Adatok elmentése osztályba
for dolgozo in adatok:
    Dolgozok(int(dolgozo[0]),dolgozo[1],dolgozo[2],dolgozo[3],dolgozo[4],int(dolgozo[5]),int(dolgozo[6]),dolgozo[7],dolgozo[8],dolgozo[9])

#Kiíratás
jutalomSum=Dolgozok.dolgozokLista[0].jutalomSum()
fiztesAtlag=Dolgozok.dolgozokLista[0].fizetesAtlag()
recskiDolgozo=Dolgozok.dolgozokLista[0].recskiDolgozo()
tataiDolgozo=Dolgozok.dolgozokLista[0].tataiDolgozo()
print(f"A jutalmak összege: {jutalomSum}\nA fizetések átlaga: {fiztesAtlag}\n{recskiDolgozo}\nEnnyi tatai dolgozó van: {tataiDolgozo}")