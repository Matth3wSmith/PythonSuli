from sys import stdin,stdout

orak = {
    1:"one",
    2:"two",
    3:"three",
    4:"four",
    5:"five",
    6:"six",
    7:"seven",
    8:"eight",
    9:"nine",
    10:"ten",
    11:"eleven",
    12:"twelve"
}
def main():
    eredetiOra,perc=list(map(int,stdin.readline().split()))
    szoveg=""
    ora=eredetiOra
    if eredetiOra>12:
        ora=eredetiOra-12

    if perc==0:
        for kulcs in orak:
            if kulcs==ora:
                szoveg+=orak[kulcs]+" o'clock"
    elif perc==30:
        for kulcs in orak:
            if kulcs==ora:
                szoveg+="half past " + orak[kulcs]
    elif perc==15:
        for kulcs in orak:
            if kulcs==ora:
                szoveg+="a quarter past "+orak[kulcs]
    else:
        for kulcs in orak:
            if kulcs==ora+1:
                szoveg+="a quarter to "+orak[kulcs]
    if eredetiOra>11:
        if eredetiOra==23 and perc==45:
            szoveg+=" a.m."

        else:
            szoveg+=" p.m."
    else:
        if ora==11 and perc==45:
            szoveg+=" p.m."
        else:

            szoveg+=" a.m."

    stdout.write(szoveg)

main()