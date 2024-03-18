#Gyártó: Kovács Máté

class Keres():
    keresesek=[]
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

    #7. feladat
    def Domain(self):
        if not Keres.keresesek[0].cim[-1].isnumeric():
            return "Van"
        else:
            return "Nincs"
        
        