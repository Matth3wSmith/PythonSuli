from sys import stdin, stdout
import math
def main():
    ropi=6
    kezi=7
    tanulok=int(stdin.readline())
    keziTanulo=0
    ropiTanulo=0
    if tanulok%kezi==6:
        keziTanulo=math.floor(tanulok/kezi)
        ropiTanulo=1
        tanulok=0
    elif tanulok%kezi<tanulok%ropi:
        keziTanulo=math.floor(tanulok/kezi)
        tanulok=tanulok%kezi
    elif tanulok%ropi<tanulok%kezi:
        ropiTanulo=math.floor(tanulok/ropi)
        tanulok=tanulok%ropi

    
    stdout.write(f"{ropiTanulo} {keziTanulo} {tanulok}")




main()