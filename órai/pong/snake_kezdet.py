#Egyszerű pong játék
#Start: 2024.01.31
#Kovács Máté

from tkinter import *
import random

def rajzol():
    labdaPos[0]+=labdaSpeed[0]*(labdaSize+2)
    labdaPos[1]+=labdaSpeed[1]*(labdaSize+2)
    szelesseg=win.winfo_width()
    magassag=win.winfo_height()
    if labdaPos[0]+labdaSize>=szelesseg or labdaPos[0]<0:
        labdaSpeed[0]*=-1
        #labdaColor=randomColor()
    elif labdaPos[1]+labdaSize>magassag or labdaPos[1]<0:
        labdaSpeed[1]*=-1
        #labdaColor=randomColor()

    labdaLista.append(canvas.create_oval(labdaPos[0],labdaPos[1],labdaPos[0]+labdaSize,labdaPos[1]+labdaSize, fill=labdaColor, outline=""))

    kajaCheck()
    utkozes()
    if len(labdaLista)==labdaListaHossz:
        canvas.delete(labdaLista[0])
        labdaLista.pop(0)

    if not halal:
        win.after(jatekSpeed,rajzol)

def randomColor():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return ("#"+hex(r)[-2:]+hex(g)[-2:]+hex(b)[-2:]).replace("x","0")

def atmenetColor(red, green, blue):
    red+=5
    if red>255:
        red-=255
        green+=5
    if green>255:
        green-=255
        blue+=5
    if blue>255:
        blue-=255
    
    return ("#"+hex(red)[-2:]+hex(green)[-2:]+hex(blue)[-2:]).replace("x","0"),red,green,blue

def gombLe(event):
    if event.keysym=="Up":
        #print("Fel")
        labdaSpeed[0]=0
        labdaSpeed[1]=-1
    elif event.keysym=="Down":
        labdaSpeed[0]=0
        labdaSpeed[1]=1
        #print("Le")
    elif event.keysym=="Right":
        labdaSpeed[0]=1
        labdaSpeed[1]=0
        #print("Right")
    elif event.keysym=="Left":
        labdaSpeed[0]=-1
        labdaSpeed[1]=0
        #print("Bal")
    #print(event)

halal=False
kajaLista=[]
def kaja():
    x=random.randint(0,win.winfo_width()-kajaSize)
    y=random.randint(0,win.winfo_height()-kajaSize)
    kajaLista.append(canvas.create_oval(x,y,x+kajaSize, y+kajaSize, fill=kajaColor, outline=""))
    win.after(kajaSpeed,kaja)
    #ÜTKÖZÉS python tkinter (part 5): Collision Detection

def kajaCheck():
    global labdaListaHossz
    f=canvas.bbox(labdaLista[-1])
    #Kígyó közepe
    fKozep=[(f[0]+f[2])/2,(f[1]+f[3])/2]
    for egyKaja in kajaLista:
        k=canvas.bbox(egyKaja)
        #Kaja közepe
        kKozep=[(k[0]+k[2])/2,(k[1]+k[3])/2]

        x=fKozep[0]-kKozep[0]
        y=fKozep[1]-kKozep[1]

        #Ha eléri a kaját
        #kajaSize és labdaSize átmérő és sugár kell!!
        if x**2+y**2 <= ((labdaSize+kajaSize)*0.5)**2:
            print("HAMMM!")
            kajaLista.remove(egyKaja)
            canvas.delete(egyKaja)
            labdaListaHossz+=1

def utkozes():
    global halal
    f=canvas.bbox(labdaLista[-1])
    #Kígyó közepe
    fKozep=[(f[0]+f[2])/2,(f[1]+f[3])/2]

    for egyLabda in labdaLista[:-1]:
        k=canvas.bbox(egyLabda)
        #Kaja közepe
        kKozep=[(k[0]+k[2])/2,(k[1]+k[3])/2]

        x=fKozep[0]-kKozep[0]
        y=fKozep[1]-kKozep[1]

        #Ha eléri a kaját
        #kajaSize és labdaSize átmérő és sugár kell!!
        if x**2+y**2 <= labdaSize**2:
            print("GAME OVER!")
            halal=True
            
#ablak létrehozása
win=Tk()

jatekHatter="lightgray"
jatekSpeed=100
kajaSpeed=2000
#ablak mérete
win.geometry("1000x600")

win.title("Pong")

#canvas létrehozás
canvas=Canvas(win, width=600, height=600, bg=jatekHatter)

#canvas akkora amekkora az ablak
canvas.pack(fill = BOTH, expand = 1)


labdaSpeed=[0,0]
labdaPos=[100,100]
labdaSize=20
kajaSize=20
labdaColor="green"
kajaColor="red"
labdaLista=[]
labdaListaHossz=3
red,green,blue=0,0,0

win.bind("<KeyPress>",gombLe)

win.after(jatekSpeed,rajzol)
win.after(kajaSpeed,kaja)

win.mainloop()
