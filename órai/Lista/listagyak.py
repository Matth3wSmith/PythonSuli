def maxKeres(lista):
    legnagyobb = lista[0]
    maxIndex = 0
    for i in range(len(szamok)):
        if szamok[i] > legnagyobb:
            legnagyobb = lista[i]
            maxIndex = i
    return(legnagyobb, maxIndex)


szamok = [100,69,35,73,55,66,33,22,46,91,16,32]

legnagyobb,maxIndex = maxKeres(szamok)


print(maxIndex, legnagyobb)
