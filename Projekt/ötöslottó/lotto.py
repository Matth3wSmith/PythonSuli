import random

#ÖTÖSLOTTÓ
otosLista = []

while len(otosLista)<= 4:
    randomSzam = random.randint(1,90);
    if randomSzam not in otosLista:
        otosLista.append(randomSzam)

print(otosLista)

#HATOSLOTTÓ
hatosLista = []

while len(hatosLista)<= 5:
    randomSzam = random.randint(1,45);
    if randomSzam not in hatosLista:
        hatosLista.append(randomSzam)

print(hatosLista)

#SKANDINÁV LOTTÓ

skandiLista = []

while len(skandiLista)<= 6:
    randomSzam = random.randint(1,35);
    if randomSzam not in skandiLista:
        skandiLista.append(randomSzam)

print(skandiLista)
