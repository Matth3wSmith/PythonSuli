#Gyártó: Kovács Máté

class Fracs():
    Titkositott=[]
    Kodlemez=[]
    Titkositando=""
    def __init__(self,kodlemez,titkositando):

        #ADATOK INICIALIZÁLÁSA
        for __ in range(8):
            tempLista=[]
            for __ in range(8):
                tempLista.append("#")
            self.Titkositott.append(tempLista)

        f=open(kodlemez,"r")
        for sor in f:
            tempLista=[]
            for elem in sor.strip():
                tempLista.append(elem)
            self.Kodlemez.append(tempLista)
        f.close()

        
        self.Titkositando=titkositando
        
        ######################

    #4. feladat
    def Atalakit(self):
        self.Titkositando=self.Titkositando.replace(" ","")
        self.Titkositando=self.Titkositando.replace(",","")
        self.Titkositando=self.Titkositando.replace(".","")
        if len(self.Titkositando)>64:
            return "Túl hosszú a titkosítandó szöveg!"
        while len(self.Titkositando)!=64:
            self.Titkositando+="X"
        return self.Titkositando

    #7. feladat
    def KiirKodlemez(self):
        for sor in self.Kodlemez:
            for elem in sor:
                print(elem,end="")
            print(end="\n")

    #9. feladat
    def ForgatKodlemez(self):
        ujKodlemez=[]
        for __ in range(8):
            tempLista=[]
            for __ in range(8):
                tempLista.append("#")
            ujKodlemez.append(tempLista)
        
        for sor in range(8):
            for oszlop in range(8):
                ujKodlemez[7-oszlop][sor] = self.Kodlemez[sor][oszlop]
        for sor in ujKodlemez:
            for elem in sor:
                print(elem,end="")
            print(end="\n")
        return ujKodlemez

    #10. feladat
    def Titkosit(self):
        betuSzamlalo=0
        print(len(self.Titkositando))
        while betuSzamlalo!=64:
            #Végigmegy a Kodlemez listáin
            for sor in self.Kodlemez:
                #Végigmegy a soron
                tempSor=sor.copy()
                for elem in tempSor:
                    if elem=="A":
                        print(elem)
                        #Megkeresi az "A" indexét
                        betuI=tempSor.index(elem)
                        betuSzamlalo+=1
                        print("Betű indexe:"+str(betuI))
                        print("Betűhossz:"+str(betuSzamlalo))
                        
                        #Utána kicseréli a Titkositottban
                        self.Titkositott[self.Kodlemez.index(sor)][betuI]=self.Titkositando[betuSzamlalo]
                        tempSor[betuI]="#"

            self.Kodlemez=self.ForgatKodlemez()
            


#5. Feladat
f=open("szoveg.txt","r")
titkositando=f.read()
f.close()
print("5. feladat:")
print(titkositando+"\n")

#6. feladat
fracs=Fracs("kodlemez.txt",titkositando)

#7.feladat
print("7. feladat")
fracs.KiirKodlemez()


#8. feladat
print("\n8. feladat:")
print(fracs.Atalakit())

#10. feladat
print("\n10. feladat")
fracs.Titkosit()
for sor in fracs.Titkositott:
    for elem in sor:
        print(elem,end="")
    print(end="\n")
