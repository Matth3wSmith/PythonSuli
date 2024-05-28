from sys import stdin, stdout,argv
#import time
def main():
	#kezdoIdo=time.time()
	#print(argv[1])
	adatok=[]
	adatKell=[]
	adatHossz=0
	with open(argv[1],"r") as f:
		napDb=list(map(int, f.readline().split()))[1]

		for sor in f:
			#print(sor)
				adatHossz+=1
				tempAdat=list(map(int, sor.split()))
				#adatok.append(list(map(int, sor.split())))
				atlag=sum(tempAdat)/napDb
				if(max(tempAdat)-atlag>atlag-min(tempAdat)):
					adatKell.append(adatHossz)
		f.close()
		

	stdout.write(str(len(adatKell)) + " " + " ".join(list(map(str, adatKell))))

	#vegIdo=time.time()
	#print("\n",vegIdo-kezdoIdo)
main()



