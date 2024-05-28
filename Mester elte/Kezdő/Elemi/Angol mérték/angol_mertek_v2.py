from sys import stdin, stdout,argv

def main():
	kiemenet=[]
	with open(argv[1],"r") as f:
		
		temp1=list(map(int,f.readline().split()))
		temp2=list(map(int,f.readline().split()))
		kiemenet=[[str(temp1[i]+temp2[i]) for i in range(len(temp1))],[str(temp1[i]-temp2[i]) for i in range(len(temp1))]]

		f.close()

	#kiemenet=[[adatok[0][i]+adatok[1][i] for i in range(len(adatok[0]))],[adatok[0][i]-adatok[1][i] for i in range(len(adatok[0]))]]
	
	stdout.write(" ".join(kiemenet[0])+"\n"+" ".join(kiemenet[1]))

main()