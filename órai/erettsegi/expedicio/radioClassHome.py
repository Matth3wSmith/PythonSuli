class Uzenet():
    uzenetek=[]
    napok=[]
    sorszamok=[]
    def __init__(self,nap,sorszam,szoveg):
        self.sorszam=sorszam
        if sorszam not in self.sorszamok:
            self.sorszamok.append(sorszam)
        self.nap=nap
        if nap not in self.napok:
            self.napok.append(nap)
        self.szoveg=szoveg
        self.uzenetek.append(self)
    
    #2. feladat
    def rogzites(self):
        """for amator in Uzenet.uzenetek:
            if amator.nap == min(self.napok):
                legkisebb=amator.sorszam"""