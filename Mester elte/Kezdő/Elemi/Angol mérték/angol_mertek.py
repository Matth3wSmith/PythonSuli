from sys import stdin, stdout,argv
import time
def main():
	adatok=[]
	"""
		for sor in f:
			temp=list(map(int,sor.split()))
			#adatok.append(list(map(int,sor.split())))
			if szamlalo==0:
				kiemenet=[temp,temp]
				szamlalo+=1
			else:
				#temp12=[([kiemenet[0][i]+temp[i]],[kiemenet[0][i]-temp[i]])for i in range(len(temp))]
				kiemenet1=[]
				kiemenet2=[]
				for i in range(len(temp)):
					kiemenet1.append(str(kiemenet[0][i]+temp[i]))
					kiemenet2.append(str(kiemenet[0][i]-temp[i]))"""
	
	with open(argv[1],"r") as f:
		for sor in f:
			adatok.append(list(map(int,sor.split())))
		f.close()

	kiemenet=[[adatok[0][i]+adatok[1][i] for i in range(len(adatok[0]))],[adatok[0][i]-adatok[1][i] for i in range(len(adatok[0]))]]
	
	stdout.write(" ".join((map(str,kiemenet[0])))+"\n"+" ".join((map(str,kiemenet[1]))))


main()