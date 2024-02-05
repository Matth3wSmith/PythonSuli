#Egyszerű pong játék
#Start: 2024.01.31
#Kovács Máté

from tkinter import *
import random

def rajzolas():
    labdaPos[0]+=labdaSpeed[0]
    labdaPos[1]+=labdaSpeed[1]
    szelesseg=win.winfo_width()
    magassag=win.winfo_height()
    if labdaPos[0]+labdaSize>=szelesseg or labdaPos[0]<0:
        labdaSpeed[0]*=-1
        #labdaColor=randomColor()
    elif labdaPos[1]+labdaSize>magassag or labdaPos[1]<0:
        labdaSpeed[1]*=-1
        #labdaColor=randomColor()

    labdaLista.append(canvas.create_oval(labdaPos[0],labdaPos[1],labdaPos[0]+labdaSize,labdaPos[1]+labdaSize, fill=labdaColor, outline=""))
    if len(labdaLista)==labdaListaHossz:
        canvas.delete(labdaLista[0])
        labdaLista.pop(0)

    
    win.after(jatekSpeed,rajzolas)

#ablak létrehozása
win=Tk()

jatekHatter="lightgray"
jatekSpeed=10

#ablak mérete
win.geometry("1000x600")

win.title("Pong")

#canvas létrehozás
canvas=Canvas(win, width=600, height=600, bg=jatekHatter)

#canvas akkora amekkora az ablak
canvas.pack(fill = BOTH, expand = 1)

labdaSpeed=[2,1]
labdaPos=[0,0]
labdaSize=50
labdaColor="green"
labdaLista=[]
labdaListaHossz=2
win.after(jatekSpeed,rajzolas)
win.mainloop()

while True:
    rajzolas()
    canvas.update()