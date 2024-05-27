from sys import stdin, stdout,argv

def main():
	#print(argv[1])
	adatok=[]
	adatKell=[]

	with open(argv[1],"r") as f:
		napDb=list(map(int, f.readline().split()))[1]

		for sor in f:
			#print(sor)
				adatok.append(list(map(int, sor.split())))
				atlag=sum(adatok[-1])/napDb
				if(max(adatok[-1])-atlag>atlag-min(adatok[-1])):
					adatKell.append(len(adatok))
		f.close()

	stdout.write(str(len(adatKell)) + " " + " ".join(list(map(str, adatKell))))
main()



