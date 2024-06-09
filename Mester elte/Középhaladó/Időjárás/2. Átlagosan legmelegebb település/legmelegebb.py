from sys import stdin, stdout

def main():
    atlagok=[]
    nap=list(map(int,input().split()))[1]
    for sor in stdin:
        atlagok.append(sum(list(map(int,sor.split())))/nap)

    stdout.write(str(atlagok.index(max(atlagok))+1))

main()