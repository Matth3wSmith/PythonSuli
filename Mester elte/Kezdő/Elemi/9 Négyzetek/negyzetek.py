from sys import stdin,stdout
import math
def main():

    negyzetek=int(stdin.readline().strip())
    oldalak=[]

    while negyzetek!=0:
        negyzet=math.floor(math.sqrt(negyzetek))
        oldalak.append(str(negyzet))
        negyzetek-=negyzet**2
    
    stdout.write(" ".join(oldalak))
main()
