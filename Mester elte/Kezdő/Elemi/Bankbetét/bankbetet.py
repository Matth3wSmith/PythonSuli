from sys import stdin, stdout

def main():
    betet,kamat,premium,honap=list(map(int,input().split()))
    otthon=0
    for egyHonap in range(honap):
        if betet>=1000:
            otthon+=int(betet*((kamat+premium)/100))
        else:
            otthon+=int(betet*(kamat/100))

        if otthon>=100:
            betet+=otthon//100*100
            otthon-=otthon//100*100

        stdout.write(str(betet)+" "+str(otthon)+"\n")

main()