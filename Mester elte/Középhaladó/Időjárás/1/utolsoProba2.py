from sys import stdin, stdout

def main2():
	adatKell=[]
	adatHossz=0
	napDb=list(map(int, input().split()))[1]

	for sor in stdin:
		adatHossz+=1
		sor=list(map(int, sor.split()))
		atlag=sum(sor)/napDb
		if(max(sor)-atlag>atlag-min(sor)):
			adatKell.append(adatHossz)
	
	stdout.write(str(len(adatKell)) + " " + " ".join(list(map(str, adatKell))))


main2()