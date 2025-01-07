from sys import stdin,stdout

def main():
    elsoTort=list(map(int,stdin.readline().split()))
    masodikTort=list(map(int,stdin.readline().split()))

    egesz=elsoTort[0]+masodikTort[0]
    #bővítés, felszorzás a nevezőkkel
    if elsoTort[2]!=masodikTort[2]:
        szamlalo=elsoTort[1]*masodikTort[2]+masodikTort[1]*elsoTort[2]
        nevezo=elsoTort[2]*masodikTort[2]
    else:
        szamlalo=elsoTort[1]+masodikTort[1]
        nevezo=elsoTort[2]
    if szamlalo!=0 and szamlalo//nevezo>0:
        egesz+=szamlalo//nevezo
        szamlalo=szamlalo%nevezo

    stdout.write(f"{egesz} {szamlalo} {nevezo}\n")

    #egész*nevező+szamlalo
    szamlalo=(elsoTort[0]*elsoTort[2]+elsoTort[1])*(masodikTort[0]*masodikTort[2]+masodikTort[1])
    nevezo=elsoTort[2]*masodikTort[2]
    egesz=szamlalo//nevezo
    szamlalo=szamlalo%nevezo
    osztando=max(szamlalo,nevezo)
    oszto=min(szamlalo,nevezo)
    if oszto!=0:
        while osztando%oszto!=0:
            tempOsztando=osztando
            osztando=oszto
            oszto=tempOsztando%oszto
        lnko=oszto
        #print(szamlalo,nevezo,lnko)
    szamlalo=round(szamlalo/lnko)
    nevezo=round(nevezo/lnko)
    stdout.write(f"{egesz} {szamlalo} {nevezo}")

main()