#Gyártó: Kovács Máté
import modul

#3. feladat
dolgozok=[]
class Dolgozo():
    def __init__(self,sor):
        self.nev=sor[0]
        self.penz=int(sor[1].split("$")[1])
        self.szuletes=int(sor[2])
        self.szekhely=sor[3]


"""#1.feladat
print("1. feladat")
szam = int(input("Írj be egy egész számot: "))
szoveg = input("Írj be egy tetszőleges szöveget: ")
print("Megoldás: {} \n".format((szoveg.upper()+" ")*szam))


#2.feladat
print("2. feladat")
halmazA,halmazB=modul.szamBekeres()
print("'A' halmza elemei: {}".format(halmazA))
print("'B' halmza elemei: {}".format(halmazB))
metszet=modul.metszet(halmazA,halmazB)
if len(metszet)==0:
    print("A két halmaz metszete üres halmaz")
else:
    print("'A'∩'B': {}".format(metszet))"""

#3. feladat
f=open("employees.txt","r")
adatok=[]
for sor in f:
    print(sor.strip().split(";"))
    dolgozok.append(Dolgozo(sor.strip().split(";")))
f.close()
#3.2
print("3.2: A cégnél {} programozó dolgozik!".format(len(dolgozok)))

atlagJovedelem=0
for dolgozo in dolgozok:
    atlagJovedelem+=dolgozo.penz
atlagJovedelem=atlagJovedelem/12/len(dolgozok)

#3.3
print("3.3: Az alkalamazottak havi átalagjövedelme: ${:.1f}".format(atlagJovedelem))

#3.4
nev=input("Adj meg egy nevet: ")
kor=0
szekhely=0
fizetes=0
for dolgozo in dolgozok:
    if dolgozo.nev==nev:
        kor=2024-dolgozo.szuletes
        szekhely=dolgozo.szekhely
        fizetes=dolgozo.penz/12*361.51
if kor!=0:
    print("\téletkor:\t{}".format(kor))
    print("\tszékhely:\t{}".format(szekhely))
    print("\thavi fizetés:\t{:.0f} HUF".format(fizetes))
else:
    print("Nincs ilyen nevű dolgozó a cégnél")