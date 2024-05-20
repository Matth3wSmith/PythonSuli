import math

def kor():
    x=int(input("X koordináta: "))
    y=int(input("Y koordináta: "))
    r=int(input("Sugár: "))
    return [x,y,r]

# r1: az első kör sugara
# r2: a második kör sugara
# d: a középpontok távolsága

# két kör érinti egymást, ha a sugaruk összege megegyezik a középpontjaik távolságával
# visszatérési értéke: logikai
def erint(r1,r2,d):
    temp=listaKeszit(r1,r2,d)
    return temp[0]+temp[1]==temp[2]

# két kör nem érinti és nem is metszi egymást, ha a sugaraik és távolságuk közül a két kisebb összege kisebb, mint a harmadik
# a körök lehetnek kívül, vagy belül is
# visszatérési értéke: logikai
def nemErint(r1,r2,d):
    temp=listaKeszit(r1,r2,d)
    return temp[0]+temp[1]<temp[2]

# két kör metszi egymást, ha a sugaraik és távolságuk közül a két kisebb összege nagyobb, mint a harmadik
# a körök lehetnek kívül, vagy belül is
# visszatérési értéke: logikai
def metsz(r1,r2,d):
    temp=listaKeszit(r1,r2,d)
    return temp[0]+temp[1]>temp[2]

# rendezi az adatokat, hogy megtudjuk melyik a leghosszabb
# visszatérési értéke: rendezett lista
def listaKeszit(r1,r2,d):
    temp=[r1,r2,d]
    temp.sort()
    return temp


def viszony(kor1,kor2):
    d=math.sqrt((kor1[0]-kor2[0])**2+(kor1[1]-kor2[1])**2)
    if nemErint(kor1[-1],kor2[-1],d):
        return "Nem érinti"
    elif erint(kor1[-1],kor2[-1],d):
        return "Erint"
    elif metsz(kor1[-1],kor2[-1],d):
        return "Metsz"