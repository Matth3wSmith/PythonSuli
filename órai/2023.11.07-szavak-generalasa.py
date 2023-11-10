import random

#SZAVAK GENERÁLÁSA

mgh = ["a", "á", "e", "é", "i", "í", "o", "ó", "ö", "ő", "u", "ú", "ü", "ű"]
msh = ["b", "d", "dz", "dzs", "g", "gy", "j", "l", "ly", "m", "n", "ny", "r", "v", "z", "zs", "c", "cs", "f", "h", "k", "p", "s", "sz", "t", "ty"]

valaszto = random.randint(0,1)
print(valaszto)
szo = ""
for i in range(0,5):
    #Mgh-val kezdünk ha a valaszto == 0
    if valaszto == 0:
        if i%2 == 0:
            index = random.randrange(0,len(mgh))
            print(index)
            szo += mgh[index]
        else:
            index = random.randrange(0,len(msh))
            szo += msh[index]
    else:
        if i%2 == 1:
            index = random.randrange(0,len(mgh))
            print(index)
            szo += mgh[index]
        else:
            index = random.randrange(0,len(msh))
            szo += msh[index]

print(szo)
