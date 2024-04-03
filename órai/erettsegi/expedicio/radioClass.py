class Uzenet():
    def __init__(self,sor1,sor2):
        self.nap=int(sor1.split(" ")[0])
        self.amator=int(sor1.split(" ")[1])

        self.uzenet=sor2
    
    def farkasKereso(self):
        return "farkas" in self.uzenet
    

class Nap:
    def __init__(self, nap):
        self.nap=nap
        self.uzenetek=[]
    
    def hozzaAd(self,uzenet):
        self.uzenetek.append(uzenet)

    def uzenetSzam(self):
        return len(self.uzenetek)