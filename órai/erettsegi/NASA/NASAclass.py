#Gyártó: Kovács Máté

class Keres():
    keresesek=[]
    kodok=[]
    kodStat={}
    cim=0
    datum=0
    kep=0
    allapot=0
    meret=0
    def __init__(self,cim,datum,kep,allapot,meret):
        self.cim=cim
        self.datum=datum
        self.kep=kep
        self.allapot=allapot
        #6. feladat
        meret=meret.strip("\n")
        if meret =="-":
            self.ByteMeret=0
        else:
            self.ByteMeret=int(meret)

        self.keresesek.append(self)

        #9. feladat
        self.kodStat[allapot]=0
            
    #7. feladat
    def Domain(self):
        
        if self.cim[-1].isnumeric()==False:
            return "Van"
        else:
            return "Nincs"
        
        #return not self.cim[-1].isnumeric()
    def allapotKodok(self):
        keys = self.kodStat.keys()
        for egyKey in keys:
            if self.allapot==egyKey:
                self.kodStat[egyKey]+=1
        return self.kodStat
