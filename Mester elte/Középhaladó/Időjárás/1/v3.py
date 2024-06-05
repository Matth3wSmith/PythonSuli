from sys import stdin, stdout,argv

def main():
	adatKell=[]
	adatHossz=0
	szoveg=""
	with open(argv[1],"r") as f:
		napDb=list(map(int, f.readline().split()))[1]

		for sor in f:
			adatHossz+=1
			sor=list(map(int, sor.split()))
			atlag=sum(sor)/napDb
			if(max(sor)-atlag>atlag-min(sor)):
				adatKell.append(adatHossz)
				szoveg+=str(adatHossz)+" "
		f.close()
	stdout.write(szoveg.strip())


main()