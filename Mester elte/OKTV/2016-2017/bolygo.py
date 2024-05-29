from sys import stdout,stdin,argv


def main():
    sor=1
    bolygok=[]
    bolygo=[]
    with open(argv[1],"r") as f:
        A,B,C=map(int,f.readline().split())
        bolygok.append([list(map(int,f.readline().split())) for i in range(A)])
        bolygok.append([list(map(int,f.readline().split())) for i in range(B)])
        bolygok.append([list(map(int,f.readline().split())) for i in range(C)])
        elet=[]
        for bolygo1 in bolygok[0]:
            for bolygo2 in bolygok[1]:
                for bolygo3 in bolygok[2]:
                    if len(set(range(bolygo1[0],bolygo1[1])).intersection(set(range(bolygo2[0],bolygo2[1]))))>0:
                        elet.append(set(range(bolygo1[0],bolygo1[1])).intersection(set(range(bolygo2[0],bolygo2[1]))))
                        continue
                    if len(set(range(bolygo1[0],bolygo1[1])).intersection(set(range(bolygo3[0],bolygo3[1]))))>0:
                        elet.append(set(range(bolygo1[0],bolygo1[1])).intersection(set(range(bolygo3[0],bolygo3[1]))))
                        continue
                    if len(set(range(bolygo2[0],bolygo2[1])).intersection(set(range(bolygo3[0],bolygo3[1]))))>0:
                        elet.append(set(range(bolygo2[0],bolygo2[1])).intersection(set(range(bolygo3[0],bolygo3[1]))))
                        continue

        print(elet)

main()