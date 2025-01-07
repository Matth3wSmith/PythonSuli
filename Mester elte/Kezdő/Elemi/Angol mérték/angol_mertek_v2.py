from sys import stdin, stdout,argv

def main():
	kiemenet=[[],[]]
	temp1=list(map(int,input().split()))
	temp2=list(map(int,input().split()))
	#kiemenet=[[str(temp1[i]+temp2[i]) for i in range(len(temp1))],[str(temp1[i]-temp2[i]) for i in range(len(temp1))]]
	for i,elso in enumerate(temp1):
		kiemenet[0].append(str(elso+temp2[i]))
		kiemenet[1].append(str(elso-temp2[i]))
	stdout.write(" ".join(kiemenet[0])+"\n"+" ".join(kiemenet[1]))

main()