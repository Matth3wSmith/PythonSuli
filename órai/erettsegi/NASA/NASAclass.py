#Gyártó: Kovács Máté

class Keres():
    keresesek=[]
    domain=0
    datum=0
    kep=0
    allapot=0
    meret=0
    def __init__(self,domain,datum,kep,allapot,meret):
        self.domain=domain
        self.datum=datum
        self.kep=kep
        self.allapot=allapot
        self.meret=meret

        self.keresesek.append(self)

