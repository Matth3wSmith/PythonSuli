from sys import stdin, stdout
import math
def main():
    kosar=5
    kezi=7
    tanulok=int(stdin.readline())
    keziTanulo=0
    kosarTanulo=0
    if tanulok%kezi==5:
        keziTanulo=math.floor(tanulok/kezi)
        kosarTanulo=1
        tanulok=0
    elif tanulok%kezi==6:
        keziTanulo=math.floor(tanulok/kezi)
        kosarTanulo=1
        tanulok=1
    elif tanulok%kezi<tanulok%kosar:
        keziTanulo=math.floor(tanulok/kezi)
        tanulok=tanulok%kezi
    elif tanulok%kosar<tanulok%kezi:
        kosarTanulo=math.floor(tanulok/kosar)
        tanulok=tanulok%kosar

    
    stdout.write(f"{kosarTanulo} {keziTanulo} {tanulok}")




main()