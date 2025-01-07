from sys import stdin,stdout
def csoportos(letszam):
    if letszam>40:
        return 14
    else:
        kedvezmeny={
            10:0,
            20:5,
            30:8,
            41:12,
        }
        for kulcs in kedvezmeny:
            if letszam<kulcs:
                return kedvezmeny[kulcs]*letszam
def iskolai(letszam):
    if letszam>40:
        return 5
    else:
        iskola={
            5:0,
            12:1,
            20:2,
            29:3,
            41:4,
        }
        for kulcs in iskola:
            if letszam<kulcs:
                return iskola[kulcs]*100

def main():
    letszam=int(stdin.readline().strip())
    diakKedv=letszam*10
    iskolai2=iskolai(letszam)
    csoportos2=csoportos(letszam)
    if(diakKedv>iskolai2 and diakKedv>csoportos2):
        stdout.write("diak")
    elif(iskolai2>diakKedv and iskolai2>csoportos2):
        stdout.write("iskolai")
    else:
        stdout.write("csoportos")
    

main()
