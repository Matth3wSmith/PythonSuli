from tkinter import *
import math
import random

#eltolás
def eltolas(pontok,x,y):
    for i in range(0,len(pontok),2):
        pontok[i]+=x
        pontok[i+1]+=y
    return pontok

def nagyit(pontok,x,y=-1):
    if y==-1:
        for i in range(len(pontok)):
            pontok[i]*=x
    else:
        for i in range(len(pontok)):
            if i%2==0:
                pontok[i]*=x
            else:
                pontok[i]*=y
    return pontok

def fasorsol(db):
    lista=[]
    temp=[]
    temp.append(random.randint(0,1))
    temp.append(random.randint(0,600))
    temp.append(random.randint(0,600))
    temp.append(random.randint(20,30)/100)


    return lista
#ablak létrehozása
win=Tk()

#ablak mérete
win.geometry("1000x1000")

#canvas létrehozás
canvas=Canvas(win, width=600, height=300)
canvas.configure(bg="lightgray")
#canvas akkora amekkora az ablak
canvas.pack(fill = BOTH, expand = 1)

pontok=[40,40,400,40,400,400,40,400,40,40]

#canvas.create_line(pontok,width=5,fill="blue")
#canvas.create_line(eltolas(pontok,100,200),width=5,fill="blue")

fenyofa=[200,0,0,400,190,400,190,500,210,500,210,400,400,400,200,0]
pontok=eltolas(fenyofa,10,10)
#canvas.create_line(pontok,width=5,fill="green")

fenyo2=[200,0,
        0,100,
        150,100,
        0,200,
        150,200,
        0,300,
        150,300,
        150,400,
        250,400,
        250,300,
        400,300,
        250,200,
        400,200,
        250,100,
        400,100,
        200,0]

fenyo2=nagyit(fenyo2,2,1)
fenyo2=eltolas(fenyo2,100,100)
canvas.create_line(fenyo2,width=5,fill="green")

win.mainloop()

