from sys import stdin, stdout

def main():
    a,b=list(map(int,stdin.readline().split()))
    x,y=list(map(int,stdin.readline().split()))
    if (b>y):
        stdout.write(f"{a*10**abs(b-y)+x} {y}\n")
        stdout.write(f"{a*10**abs(b-y)-x} {y}\n")
        stdout.write(f"{a*x} {b+y}")
    else:
        stdout.write(f"{a+x*10**abs(b-y)} {b}\n")
        stdout.write(f"{a-x*10**abs(b-y)} {b}\n")
        stdout.write(f"{a*x} {b+y}")




main()