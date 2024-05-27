from sys import stdin, stdout,argv

def main():
	adatok=[]
	
	with open(argv[1],"r") as f:
		for sor in f:
			adatok.append(list(map(int,sor.split())))
		f.close()

	kiemenet=[[adatok[0][i]+adatok[1][i] for i in range(len(adatok[0]))],[adatok[0][i]-adatok[1][i] for i in range(len(adatok[0]))]]
	
	stdout.write(" ".join((map(str,kiemenet[0])))+"\n"+" ".join((map(str,kiemenet[1]))))


main()