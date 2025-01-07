from sys import stdin,stdout

def main():
    gyufa=int(input())
    haromszogek=[]
    A=1
    for szam in range(gyufa-A):
        for i in range(gyufa-A):
            B=szam
            C=gyufa-(B+A)
            if A+B>C and A+C>B and B+C>A:
                haromszogek.append([A,B,C])
                stdout.write(" ".join(list((map(str,[A,B,C]))))+"\n")
                break
        A+=1


main()