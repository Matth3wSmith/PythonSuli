from sys import stdin, stdout,argv
import time
def main():
	kezdoIdo=time.time()

	adatok=[]
	szamlalo=0
	kiemenet=[]
	with open(argv[1],"r") as f:
		for sor in f:
			temp=list(map(int,sor.split()))
			#adatok.append(list(map(int,sor.split())))
			if szamlalo==0:
				kiemenet=[temp,temp]
				szamlalo+=1
			else:
				temp1=[]
				temp2=[]
				for i in range(len(temp)):
					temp1.append(kiemenet[0][i]+temp[i])
					temp2.append(kiemenet[0][i]-temp[i])
				kiemenet[0]=temp1
				kiemenet[1]=temp2

		f.close()

	#kiemenet=[[adatok[0][i]+adatok[1][i] for i in range(len(adatok[0]))],[adatok[0][i]-adatok[1][i] for i in range(len(adatok[0]))]]
	
	stdout.write(" ".join((map(str,kiemenet[0])))+"\n"+" ".join((map(str,kiemenet[1]))))
	vegIdo=time.time()
	print("\n",vegIdo-kezdoIdo)


main()