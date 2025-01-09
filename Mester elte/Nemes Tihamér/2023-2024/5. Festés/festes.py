from sys import stdin,stdout

def main():

    sor,oszlop=map(int,stdin.readline().split())
    koltsegek=list(map(int,stdin.readline().split()))
    tablazat=[]
    for i in range(oszlop):
        tablazat.append(list(map(int,stdin.readline().split())))

    print(tablazat)
main()