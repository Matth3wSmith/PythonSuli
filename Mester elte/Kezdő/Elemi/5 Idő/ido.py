from sys import stdin,stdout

def main():
	hour,minute,sec,hSec=list(map(int,input().split()))
	hour2,minute2,sec2,hSec2=list(map(int,input().split()))

	sec2+=hSec2//100
	hSec2%=100
	
	minute2+=sec2//60
	sec2%=60

	hour2+=minute2//60
	minute2%=60

	bHour= hour-hour2
	bMinute= minute-minute2
	bSec=sec-sec2
	bHSec=hSec-hSec2
	if bHSec<0:
		bSec-=1
		bHSec+=100
	if bSec<0:
		bMinute-=1
		bSec+=60
	if bMinute<0:
		bHour-=1
		bMinute+=60
	if bHour<0:
		bHour=bHour%24+24


	aHour= hour+hour2
	aMinute= minute+minute2
	aSec=sec+sec2
	aHSec=hSec+hSec2

	if aHSec>=100:
		aSec+=1
		aHSec-=100
	if aSec>=60:
		aMinute+=1
		aSec-=60
	if aMinute>=60:
		aHour+=1
		aMinute-=60
	if bHour>=24:
		bHour=bHour%24-24
	
	stdout.write(" ".join(list(map(str,[bHour,bMinute,bSec,bHSec])))+"\n"+" ".join(list(map(str,[aHour,aMinute,aSec,aHSec]))))
main()