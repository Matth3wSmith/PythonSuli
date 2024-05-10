class Versenyzo:
    def __init__(self,sor):
        vag=sor.strip().split(";")
        self.nev=vag[0]
        self.nem=vag[1]
        self.szuletes=vag[2]
        self.uszas=vag[3]
        self.kerekpar=vag[4]
        self.futas=vag[5]
        self.rajt=int(vag[6])

    def orakToMpOssz(self):
        osszIdo=0
        for ido in [self.uszas,self.kerekpar,self.futas]:
            orak=ido.split(":")
            osszIdo+=int(orak[0])*60*60+int(orak[1])*60+int(orak[2])
        return osszIdo
    def mpToOrakOssz(self):
        mpIdo=self.orakToMpOssz()
        return "{:02}:{:02}:{:02}".format(mpIdo//3600,mpIdo%3600//60,mpIdo%3600%60)
#2. feladat
versenyzok=[]
f=open("triatlon.txt","r")

next(f)
for sor in f:
    versenyzok.append(Versenyzo(sor))

f.close()

print("2. feladat")
print("A versenyen {} induló volt.".format(len(versenyzok)))

#3. feladat
gyoztesRajt=0
gyoztesVersenyzo=0
gyoztesIdo=0
tempGyoztesIdo=100000000000000000
print(versenyzok[0].orakToMpOssz())
for versenyzo in versenyzok:
    versenyzoIdo=versenyzo.orakToMpOssz()
    if tempGyoztesIdo>versenyzoIdo:
        tempGyoztesIdo=versenyzoIdo
        gyoztesRajt=versenyzo.rajt
        gyoztesVersenyzo=versenyzo.nev
        gyoztesIdo=versenyzo.mpToOrakOssz()


print("3. feladat: A verseny nyertese:")
print("\tneve: {}".format(gyoztesVersenyzo))
print("\trajtszáma: {}".format(gyoztesRajt))
print("\tösszideje: {}".format(gyoztesIdo))

#4. feladat
f=open("osszidok.txt","w")
for versenyzo in versenyzok:
    f.write("{};{};{}\n".format(versenyzo.rajt,versenyzo.nev,versenyzo.mpToOrakOssz()))
f.close()
