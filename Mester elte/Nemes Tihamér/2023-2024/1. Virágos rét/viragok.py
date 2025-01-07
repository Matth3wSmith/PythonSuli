from sys import stdin,stdout

def main():
    ret,latogatni=list(map(int,stdin.readline().split()))
    retek=stdin.readline().count("1")-(latogatni-1)

    if retek>0:
        latogatott=int((retek*(retek+1))/2)
    else:
        latogatott=0

    stdout.write(str(latogatott))


        


main()